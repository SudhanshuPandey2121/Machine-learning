# -*- coding: utf-8 -*-
"""textual preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iT_eUYckfqrkQSakIpvU0wK6JCrP77pz
"""

import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords #stopwords are irrelevant frequenty occuring words
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

news = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/train (1).csv')

from google.colab import drive
drive.mount('/content/drive')

news.head()

nltk.download('stopwords')

print(stopwords.words('english'))

"""Data-preprocessing  
0--> real news  
1--> fake news
"""

news.shape

news['label'].value_counts()

#checking for missing values
news.isnull().sum()

#replacing missing values with null string
news = news.fillna('')

news.isnull().sum()

#merging authorname and news title
news['content'] = news['author']+' '+news['title']

news.head()

#seperating features and target
x = news.drop(columns='label',axis=1)
y= news['label']

print(x.head())

"""Stemming  
the process of reducing word to its root word
"""

stemmer =PorterStemmer()

"""Defining the stemming function"""

def stemming(content):
    if isinstance(content, str):  # Check if content is a string
        stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
        stemmed_content = stemmed_content.lower()
        stemmed_content = stemmed_content.split()
        stemmed_content = [stemmer.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
        stemmed_content = ' '.join(stemmed_content)
        return stemmed_content
    else:
        return ""

news['content']=news['content'].apply(stemming)

news['content']

news.head()

#seperating in feature and target
x = news['content']
y= news['label']

print(x)

y.shape

#converting textual data to feature numbers
vectorizer = TfidfVectorizer()

# Join the tokenized words back into sentences before fitting
x_joined = [' '.join(tokens) for tokens in x_list]
vectorizer.fit(x_joined)

# Transform the joined sentences
x = vectorizer.transform(x_joined)

