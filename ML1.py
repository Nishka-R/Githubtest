#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:16:40 2017

@author: nishkaranjan
"""

# -*- coding: utf-8 -*-
# importing library and files


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#importing the dataset
dataset=pd.read_csv('/Users/nishkaranjan/Desktop/Supply Chain/Data_Preprocessing/Data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values
# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN', strategy='mean')
imputer=imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

#Encoding categorical data

from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x = LabelEncoder()
x[:,0] = labelencoder_x.fit_transform(x[:,0])
onehotencoder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#Splitting the dataset into Training set and Test Set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 0)

# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

import os
os.getcwd()
os.chdir("/Users/nishkaranjan/Documents/GitHub")
os.getcwd()

ls