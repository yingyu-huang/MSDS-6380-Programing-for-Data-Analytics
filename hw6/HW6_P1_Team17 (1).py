# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:59:53 2019

@author: Team 17
"""

import pandas as pd
import numpy as np
Train_data = pd.read_excel('titanic_traning.xlsx', na_values=['NULL'])
# Define a function, oneR, to learn from the training set
def OneR(x):
    suv_rate = pd.DataFrame(Train_data.groupby(x).survived.mean()).reset_index()
    idx = suv_rate[suv_rate.survived>0.5]
    idxr = np.array(idx)
    print('if the passenger is',idxr[:,0],'in', str(x), 's/he survived')
 # Show the results from training -- of each feature, which class leads to survival       
OneR("gender")
OneR("pclass")
OneR("sibsp")
OneR("parch")
OneR("embarked")

# Read the test set
Test_data = pd.read_excel('titanic_test.xlsx', na_values=['NULL'])
# Show the classes within each features, to facilitate modifications later
print(Test_data['gender'].unique())
print(Test_data['pclass'].unique())
print(Test_data['sibsp'].unique())
print(Test_data['parch'].unique())
print(Test_data['embarked'].unique())
# Output destination file
writer = pd.ExcelWriter('titanic_test_predictions.xlsx', engine='xlsxwriter')

# Predict survival results of test set, based on the training results
changeforgender = pd.DataFrame(Test_data.gender)  # work on the feature of gender
CFG = changeforgender.replace({'gender': {'female': 1, 'male': 0}}) # 0 means 'not survived'
GBP = pd.read_excel('titanic_test_predictions.xlsx', sheet_name='Gender_Based_Prediction')
GBP.Prediction = CFG   #add the prediction results to the output file
GBP.to_excel(writer, sheet_name='Gender_Based_Prediction', index=False)
# For gender model, calculate the %correctness of prediction
s1 = ("{0:.2%}".format(sum(GBP.iloc[:,1] == GBP.iloc[:,2])/len(GBP)))

# The rest of analysis is similar as above

changeforpclass = pd.DataFrame(Test_data.pclass) # ticket class
CFP = changeforpclass.replace({'pclass':{2:0,3:0}})
PBP = pd.read_excel('titanic_test_predictions.xlsx', sheet_name='pclass_Based_Prediction')
PBP.Prediction = CFP
PBP.to_excel(writer, sheet_name='pclass_Based_Prediction', index=False)
s2 = ("{0:.2%}".format(sum(PBP.iloc[:,1] == PBP.iloc[:,2])/len(PBP)))

changeforsibsp = pd.DataFrame(Test_data.sibsp) # number of siblings and spouses
CFS = changeforsibsp.replace({'sibsp':{2:0,3:0,4:0,5:0,8:0}})
SBP = pd.read_excel('titanic_test_predictions.xlsx', sheet_name='sibsp_Based_Prediction')
SBP.Prediction = CFS
SBP.to_excel(writer, sheet_name='sibsp_Based_Prediction', index=False)
s3 = ("{0:.2%}".format(sum(SBP.iloc[:,1] == SBP.iloc[:,2])/len(SBP)))

changeforembarked = pd.DataFrame(Test_data.embarked) # port of embarkation
CFE = changeforembarked.replace({'embarked':{'C':1,'Q':0,'S':0, ' ':0}})
PBP = pd.read_excel('titanic_test_predictions.xlsx', sheet_name='embarked_Based_Prediction')
PBP.Prediction = CFE
PBP.to_excel(writer, sheet_name='embarked_Based_Prediction', index=False)
s4 = ("{0:.2%}".format(sum(PBP.iloc[:,1] == PBP.iloc[:,2])/len(PBP)))

changeforparch = pd.DataFrame(Test_data.parch) # number of parents or children
CFPA = changeforparch.replace({'parch':{2:1,3:1,4:0,5:0,6:0}})
PABP = pd.read_excel('titanic_test_predictions.xlsx', sheet_name='parch_Based_Prediction')
PABP.Prediction = CFPA
PABP.to_excel(writer, sheet_name='parch_Based_Prediction', index=False)
s5 = ("{0:.2%}".format(sum(PABP.iloc[:,1] == PABP.iloc[:,2])/len(PABP)))

# Compute all the success rates for the test set
SRATE = pd.read_excel('titanic_test_predictions.xlsx', sheet_name='Prediction_Success_Rate')
SRATE.iloc[:,1] = [s1, s2, s3, s4, s5]
SRATE.to_excel(writer, sheet_name='Prediction_Success_Rate', index=False)
writer.close()
writer.save()