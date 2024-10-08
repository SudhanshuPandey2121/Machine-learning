# -*- coding: utf-8 -*-
"""rock vs mine prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14I5fxg0hv5p-JCp4WwqigwdFloOdZKT_
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and pre-processing

"""

mr_data = pd.read_csv('/content/sonar data.csv',header= None)

mr_data.shape

mr_data.head()

mr_data[60].value_counts()

mr_data.describe()

"""M --> Mine  
R --> Rock
"""

mr_data.groupby(60).mean()

#seperating data and label
x= mr_data.drop(columns=60,axis=1)
y=mr_data[60]

x

"""Training and test data"""

#splitting it into training and test
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,stratify=y,random_state=1)

print(x_train.shape,y_test.shape)

"""Model training ---> logistic regression"""

model = LogisticRegression()

"""Training logistical regression model with training data

"""

model.fit(x_train,y_train)

"""Evaluating our model by checking its accuracy score"""

# accuracy on training data
x_train_prediction = model.predict(x_train)
training_accuracy = accuracy_score(x_train_prediction,y_train)

training_accuracy

# accuracy on testing data
x_test_prediction = model.predict(x_test)
testing_accuracy = accuracy_score(x_test_prediction,y_test)

testing_accuracy

"""Making a predictive system"""

input_data=(0.0283,0.0599,0.0656,0.0229,0.0839,0.1673,0.1154,0.1098,0.1370,0.1767,0.1995,0.2869,0.3275,0.3769,0.4169,0.5036,0.6180,0.8025,0.9333,0.9399,0.9275,0.9450,0.8328,0.7773,0.7007,0.6154,0.5810,0.4454,0.3707,0.2891,0.2185,0.1711,0.3578,0.3947,0.2867,0.2401,0.3619,0.3314,0.3763,0.4767,0.4059,0.3661,0.2320,0.1450,0.1017,0.1111,0.0655,0.0271,0.0244,0.0179,0.0109,0.0147,0.0170,0.0158,0.0046,0.0073,0.0054,0.0033,0.0045,0.0079)
#changing inputdata to numpy array
input_data_array = np.asarray(input_data)
#reshape the np array as we are predicting for one instance
input_data_reshaped =input_data_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
if prediction=='R':
  print('It is a rock')
else:
  print('it is a mine')

input_data=(0.0235,0.0291,0.0749,0.0519,0.0227,0.0834,0.0677,0.2002,0.2876,0.3674,0.2974,0.0837,0.1912,0.5040,0.6352,0.6804,0.7505,0.6595,0.4509,0.2964,0.4019,0.6794,0.8297,1.0000,0.8240,0.7115,0.7726,0.6124,0.4936,0.5648,0.4906,0.1820,0.1811,0.1107,0.4603,0.6650,0.6423,0.2166,0.1951,0.4947,0.4925,0.4041,0.2402,0.1392,0.1779,0.1946,0.1723,0.1522,0.0929,0.0179,0.0242,0.0083,0.0037,0.0095,0.0105,0.0030,0.0132,0.0068,0.0108,0.0090)
#changing inputdata to numpy array
input_data_array = np.asarray(input_data)
#reshape the np array as we are predicting for one instance
input_data_reshaped =input_data_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
if prediction=='R':
  print('It is a rock')
else:
  print('it is a mine')

