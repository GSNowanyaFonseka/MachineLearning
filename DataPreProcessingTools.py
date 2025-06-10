# importing libraries
import numpy as np   #library in python for numerical and scientific computing
import matplotlib.pyplot as plt   #library in python for plotting graphs
import pandas as pd   #library in python for data manipulation and analysis

# importing dataset
dataset  = pd.read_csv('Data.csv')   #reading the dataset from a csv file
x = dataset.iloc[:, :-1].values  #getting all the columns except the last one    matrix of features X
y = dataset.iloc[:,-1].values  #getting the last column    vector of labels Y

print(x)
print(y)


#Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:,1:3])
x[:, 1:3] = imputer.transform(x[:,1:3])

print(x)

# Encoding categorical data
# Encoding the independant Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

print(x)