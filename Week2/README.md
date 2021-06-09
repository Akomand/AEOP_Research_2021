# Week 2 Materials
## Introduction to Natural Language Processing
### MONDAY (Text preprocessing and word embeddings)
We will be going over text preprocessing techniques including 
- Tokenization
- Denoising text w/ Regex
- Removing stopwords
- Stemming
- Lemmatization
- Term Frequency Inverse Document Frequency (TF-IDF)
- Continuous Bag-of-words and Skip-gram
- Word Embeddings (Word2Vec)

Slides: https://dijkstra.eecs.umich.edu/eecs498/lectures/l2.pdf <br>
Suggested Reading (Word2Vec): https://arxiv.org/pdf/1301.3781.pdf


### TUESDAY (Topic Modeling)
Part I: We will deep dive into what topic modeling is and its use-cases. We'll look at a specific topic modeling technique known as Latent Dirichlet Allocation (LDA) to mine topics from a corpus.

Part II: We will disect apart the "A Very Brief Introduction to Machine Learning" paper and the below paper on Latent Dirichlet Allocation.

Slides: http://www.cs.columbia.edu/~blei/talks/Blei_ICML_2012.pdf <br>
Suggested Reading (LDA): https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf <br>
Assignment: Research a paper on a topic of your choice in the field of NLP from the following list
- Sentiment Analysis
- Machine Translation
- Named Entity Recognition
- Question Answering


### WEDNESDAY (Sequence Models)
Part I: We will look at sequence models for NLP such as the Recurrent Neural Network (RNN) and a special variant called Long-Short Term Memory (LSTM) and apply them
to the task of text classification and machine translation given a corpora of text.

Part II: We will disect the below suggested paper on Recurrent Neural Networks (RNNs):

Code: https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html <br>
Suggested Reading (RNNs): https://arxiv.org/pdf/1912.05911.pdf

### THURSDAY (Transfer Learning)

Part I: We will look into the state-of-the-art in NLP known as Transformers and apply them to the task of sentiment analysis. We'll look at specific transformers including:
- Bidirectional Encoder Representations for Transformers (BERT)
- Embeddings for Language Models (ELMo)
- BERTweet
- T5

Suggested Reading (BERT Explained): https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270
