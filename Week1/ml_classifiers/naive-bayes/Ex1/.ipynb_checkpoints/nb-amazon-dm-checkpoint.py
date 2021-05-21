#!/usr/bin/env python
# coding: utf-8

# # Sentiment Analysis on Amazon-Cell Dataset using Naive Bayes



# Basic Libraries
import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
from argparse import Namespace

# Text Preprocessing
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from wordcloud import WordCloud,STOPWORDS
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize,sent_tokenize
from bs4 import BeautifulSoup
import spacy
import re,string,unicodedata
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize import RegexpTokenizer

# Model, Visualization, and Evalutation
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB, ComplementNB, BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from textblob import TextBlob
from textblob import Word
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

# Stop words
stopword_list = stopwords.words('english')




# Define argument variables
args = Namespace(
    dataset = "./data/amazon_cells_labelled.txt",
    data_type = 'text',
    task = 'Sentiment Analysis',
    model_type = "Multinomial Naive Bayes",
    train_split = 0.8,
    test_split = 0.2,
    test_sentence = 'the mic is bad',
    sentiment = {0: 'negative', 1: 'positive'}
)

print(f'Dataset: {args.dataset}\nType: {args.data_type}\nTask: {args.task}\nModel: {args.model_type}\n')


# Tokenizer
tokenizer = ToktokTokenizer()


# Function to load data
def load_data():
    data = pd.read_csv(args.dataset, sep='\t', header=None)
    data.columns = ['reviews', 'sentiment']
    
    return data



# Split data into train and test
def split_data(data):
    X_train, X_test, Y_train, Y_test = train_test_split(data['reviews'], data['sentiment'], test_size=args.test_split, random_state=5)
    
    return X_train, X_test, Y_train, Y_test



# ## Text Preprocessing

# Preprocessing Functions
# functions for removing html strips
def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

# removing square brackets
def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

# removing noisy text
def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    return text

# remove special characters
def remove_special_characters(text, remove_digits=True):
    pattern = r'[^a-zA-z0-9\s]'
    text = re.sub(pattern, '', text)
    return text

# Stemming the text
def simple_stemmer(text):
    ps=nltk.porter.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text

# Removing stopwords
def remove_stopwords(text, is_lower_case=False):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text


def preprocessing(data):
    data['reviews'] = data['reviews'].apply(denoise_text)
    data['reviews'] = data['reviews'].apply(remove_special_characters)
    data['reviews'] = data['reviews'].apply(simple_stemmer)
    data['reviews'] = data['reviews'].apply(remove_stopwords)
    
    return data


# Load Data
data = load_data()

# Preprocess data
data = preprocessing(data)


# Get train and test splits
X_train, X_test, Y_train, Y_test = split_data(data)


# Create BOW Count Vectorizer and use for embedding
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv=CountVectorizer(stop_words='english', ngram_range=(1,2))
cv_train_reviews=cv.fit_transform(X_train)
cv_train_reviews = cv_train_reviews.toarray()
cv_test_reviews=cv.transform(X_test)
cv_test_reviews.shape



# Initialize and fit NB model
model = MultinomialNB()
model.fit(cv_train_reviews, Y_train)


# Predict on training data
prediction=model.predict(cv_test_reviews.toarray())


# ## Testing & Evaluation Metrics
print()
accuracy = accuracy_score(Y_test,prediction)

print(f'Model Test Accuracy: {accuracy*100}%')


word = u'This product is bad'
test = pd.Series(word)



test = cv.transform(test)

pred = model.predict(test)


print(f'Prediction for \'{word}\': {args.sentiment[pred[0]]}')

print()

print('Classification Report for Classification')

report=classification_report(Y_test.to_numpy(),prediction,target_names=['Negative','Positive'])



print(report)


# ## Visualization


#word cloud for positive review words
plt.figure(figsize=(10,10))
spam_text=X_train[1]
WC=WordCloud(width=1000,height=500,max_words=500,min_font_size=5)
spam_words=WC.generate(spam_text)
plt.imshow(spam_words,interpolation='bilinear')
plt.show




