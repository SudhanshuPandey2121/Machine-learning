# -*- coding: utf-8 -*-
"""spam_mail_detector.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16zGgV6Xd13ALOjFQ-W6qieh0dknnNeUs
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

mail = pd.read_csv('/content/mail_data.csv')

mail.head()

mail['Category'].value_counts()

mail.isnull().sum()

#replacing null values (if exist)
mail_data = mail.where((pd.notnull(mail)),'')

mail_data.shape

"""LABEL ENCODING"""

encoder = LabelEncoder()

labels =encoder.fit_transform(mail_data.Category)
mail_data['target']=labels

mail_data.head()

"""0 --> ham  
1 --> spam
"""

#user defined label encoding
mail_data.loc[mail_data['Category']== 'spam','Category',] = 0
mail_data.loc[mail_data['Category']== 'ham','Category',] = 1

mail_data.head()

mail_data = mail_data.drop(columns = 'target',axis=1)

#seperating text and label
x = mail_data['Message']
y = mail_data['Category']

print(x,y)

"""Train test data"""

x_train, x_test , y_train, y_test = train_test_split(x,y,stratify=y,test_size=0.2,random_state=3)

#transform text to feature that can be used by logisticRegression
feature_extraction= TfidfVectorizer(min_df=1, stop_words='english',lowercase= True)
x_train_feat = feature_extraction.fit_transform(x_train)
x_test_feat = feature_extraction.transform(x_test)

print(x_train_feat)

#convert y_train y_test as integer
y_train = y_train.astype('int')
y_test = y_test.astype('int')

"""Training the model"""

model = LogisticRegression()
model.fit(x_train_feat,y_train)

"""Evaluating the trained model"""

#evaluating training prediction
training_prediction = model.predict(x_train_feat)
accuracy= accuracy_score(training_prediction,y_train)
print(accuracy)

#evaluating testing prediction
testing_prediction = model.predict(x_test_feat)
accuracy= accuracy_score(testing_prediction,y_test)
print(accuracy)

# classifying whether an input mail is spam or ham
input_mail=["Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat..."]
input_feat_mail = feature_extraction.transform(input_mail)
result= model.predict(input_feat_mail)
if result==0:
  print("Mail is a spam")
else:
  print("Mail is a ham")

