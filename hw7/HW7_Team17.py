# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:06:10 2019

@author: yingy
"""

import pandas as pd
import numpy as np
# Read-in data
data=pd.read_csv("C:/Users/yingy/Desktop/52 python/hw7/titanic_traning.csv")

## Take a look at missing and inconsistency values:
print(data['pclass'].unique())
print(data['sex'].unique())    # inconsistency
print(data['age'].unique())    # missing values
print(data['sibsp'].unique())
print(data['parch'].unique())
print(data['fare'].unique())     # missing values
print(data['embarked'].unique())  # inconsistency
print(data['survived'].unique())

#missing value of age
pd.isnull(data["age"])
c1=sum(pd.isnull(data["age"]))
c1p="{0:.2%}".format(c1/916)
#missing value of fare
pd.isnull(data["fare"])
c2=sum(pd.isnull(data["fare"]))
c2p="{0:.2%}".format(c2/916)
#inconsistent value of sex
x1=np.sum(data["sex"]=='Male')
x2=np.sum(data["sex"]=='Female')
x3=x1+x2 
x3p="{0:.2%}".format(x3/916) 

#inconsistent value of embarked
data["embarked"]=='Queenstown'
x4=np.sum(data["embarked"]=='Queenstown')
x4p="{0:.2%}".format(x4/916)  

#generate a table of missing value and inconsistent value
print('Features','MV','%ofMV','IV','%ofIV')
print('pclass  ',0.00,0.00,0.00,0.00)
print('sex     ',0.00,0.00,x3,x3p)
print('age     ',c1,c1p,0.00,0.00)
print('sibsp   ',0.00,0.00,0.00,0.00)
print('parch   ',0.00,0.00,0.00,0.00)
print('fare    ',c2,c2p,0.00,0.00)
print('embarked',0.00,0.00,x4,x4p)
print('survived',0.00,0.00,0.00,0.00)

#List/Display all the records with missing value(s) and/or inconsistent value(s).
print(data[data['age'].isnull()])
print(data[data['fare'].isnull()])

print(data[data['sex'].isin(['Male','Female'])])
print(data[data.embarked =='Queenstown'])

#Handle the missing values 
Newdata = pd.read_csv("C:/Users/yingy/Desktop/52 python/hw7/titanic_traning.csv")
changeforage = pd.DataFrame(data.age)  # work on the missing values of age
CFA = changeforage.fillna(data.mean())
Newdata.age = CFA

changeforfare = pd.DataFrame(data.fare)  # work on the missing values of fare
CFF = changeforfare.fillna(data.mean())
Newdata.fare = CFF


#Correct the data inconsistency issue
changeforsex = pd.DataFrame(data.sex)  # work on the inconsistency of sex
CFS = changeforsex.replace({'sex': {'Male':'male', 'Female':'female'}})
Newdata.sex = CFS

changeforemb = pd.DataFrame(data.embarked)  # work on the inconsistency of emb
CFE = changeforemb.replace({'embarked': {'Queenstown':'Q'}})
Newdata.embarked = CFE

#Store the clean data in a csv file
Newdata.to_csv('C:/Users/yingy/Desktop/52 python/hw7/NewData.csv')
