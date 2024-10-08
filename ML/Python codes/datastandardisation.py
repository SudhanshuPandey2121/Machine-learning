# -*- coding: utf-8 -*-
"""DataStandardisation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_II-ksp5YXYqdneT3fxKkmlq_sYGeJCC

DATA STANDARDIZATION to a common format and range
"""

import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#loading the dataset
dataset=sklearn.datasets.load_breast_cancer()

print(dataset)

#loading data to pandas
df=pd.DataFrame(dataset.data,columns=dataset.feature_names)

df.head()

df.shape

x=df
y=dataset.target

print(y)

"""Splitting the data into training and test"""

X_train,X_test,Y_train,Y_test= train_test_split(x,y,test_size=0.2,random_state=3)

print(x.shape,X_train.shape,X_test.shape)

"""Standardising data"""

print(dataset.data.std())

scaler=StandardScaler()

scaler.fit(X_train)

X_train_standardised= scaler.transform(X_train)

print(x)

print(X_train_standardised)

X_test_standardised = scaler.transform(X_test)

print(X_train_standardised.std())

print(X_test_standardised.std())

