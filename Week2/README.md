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

Introduction to NLP [[Slides](https://dijkstra.eecs.umich.edu/eecs498/lectures/l2.pdf)] <br>
Suggested Reading (Word2Vec): "Efficient Estimation of Word Representations in Vector Space" [[Paper](https://arxiv.org/pdf/1301.3781.pdf)]


### TUESDAY (Topic Modeling)
Part I: We will deep dive into what topic modeling is and its use-cases. We'll look at a specific topic modeling technique known as Latent Dirichlet Allocation (LDA) to mine topics from a corpus.

Part II: We will disect apart the "A Very Brief Introduction to Machine Learning" paper and the below paper on Latent Dirichlet Allocation.

Probabilistic Topic Models [[Slides](http://www.cs.columbia.edu/~blei/talks/Blei_ICML_2012.pdf)] <br>
Suggested Reading (LDA): "Latent Dirichlet Allocation" [[Paper](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf)] <br>
Assignment: Research a paper on a topic of your choice in the field of NLP from the following list
- Sentiment Analysis
- Machine Translation
- Named Entity Recognition
- Question Answering


### WEDNESDAY (Sequence Models)
Part I: We will look at sequence models for NLP such as the Recurrent Neural Network (RNN) and a special variant called Long-Short Term Memory (LSTM) and apply them
to the task of text classification and machine translation given a corpora of text.

Part II: We will disect the below suggested paper on Recurrent Neural Networks (RNNs):

Suggested Reading (RNNs): Recurrent Neural Networks (RNNs): A gentle Introduction and Overview [[Paper](https://arxiv.org/pdf/1912.05911.pdf)] <br>
Character Level Text Classification [[Code](https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html)] <br>
Machine Translation [[Code](https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html)] <br>
Visualizing Attention: "Mechanics of Seq2seq Models With Attention" [[Article](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)] <br>
"An intuitive explanation of Beam Search" [[Article](https://towardsdatascience.com/an-intuitive-explanation-of-beam-search-9b1d744e7a0f)]

### THURSDAY (Transformers)

Part I: We will talk about transformers from the "Attention is all you need" paper and discuss their effectiveness over regular RNNs and LSTMs. We will also deep dive into the Transformer architecture and its various components.

Suggested Reading (Transformers): "Attention is All You Need" [[Paper](https://arxiv.org/pdf/1706.03762.pdf)] [[Illustration](https://jalammar.github.io/illustrated-transformer/)] [[Code](https://pytorch.org/tutorials/beginner/transformer_tutorial.html)] <br>

### FRIDAY (Transfer Learning)

Part I: We will talk about pretrained transformer-based models such as BERT (Bidirectional Encoder Representations for Transformers) and ALBERT and discuss how we can fine-tune these models for any task we want using the HuggingFace library.

Suggested Reading: "Pre-trained Models for Natural Language Processing: A Survey" [[Paper](https://arxiv.org/pdf/2003.08271.pdf)] <br>
BERT paper: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding" [[Paper](https://arxiv.org/pdf/1810.04805.pdf)] [[Illustration](http://jalammar.github.io/illustrated-bert/)] <br> 
BERT Explained [[Article](https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270)] <br>

#### Other pretrained language models
"RoBERTa: A Robustly Optimized BERT Pretraining Approach" [[Paper](https://arxiv.org/pdf/1907.11692.pdf)] <br>
"ELMo: Deep contextualized word representations" [[Paper](https://arxiv.org/pdf/1802.05365.pdf)] <br>
"Big Bird: Transformers for Longer Sequences" [[Paper](https://arxiv.org/pdf/2007.14062.pdf)] <br>
"XLNet: Generalized Autoregressive Pretraining for Language Understanding" [[Paper](https://arxiv.org/pdf/1906.08237.pdf)]

Implementations: HuggingFace Transformers Library [[Link](https://huggingface.co/transformers/)]

Assignment: Over the weekend, find 2 papers (published in 2018 or later) covering the Question Answering task in Natural Language Processing using either Sequence models, Transformers, or some other unique technique. You can start with Google Scholar, but also try to use Connected Papers to search for these papers since it returns the most relevant and recent papers as well as those related.
