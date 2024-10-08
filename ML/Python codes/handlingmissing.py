# -*- coding: utf-8 -*-
"""handlingmissing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fkBrT9lOdIURHQWFsmIdXrxoltAuF7Em

Methods to handle missing values

1.imputation

2.Dropping
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

placement=pd.read_csv('/content/Placement_Dataset.csv')

placement.head()

#number of null values
placement.isnull().sum()

placement.shape

"""#IMPUTATION

Central tendencies
1. Mean
2. median
3. mode
"""

sns.displot(placement.salary)

"""replacing missing values with median"""

#the above graph is a screwed one that is there are some outliers that may affect the mean value
#and make it insignificant thus we cant replace the null values with mean
placement['salary'].fillna(placement['salary'].median(),inplace=True)

placement.isnull().sum()

placement.head()

"""#DROPPING
can be done in large dataset
"""

x=pd.read_csv('/content/Placement_Dataset.csv')

x.shape

x.isnull().sum()

#drop missing values
x=x.dropna(how='any')

x.shape

