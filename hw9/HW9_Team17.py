# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 23:17:39 2018

@author: Team 17
"""

import pandas as pd
from datetime import datetime

student = pd.read_excel('Student.xlsx',index_col=None)
tutor = pd. read_excel('Tutor.xlsx',index_col=None)
match = pd.read_excel('Match_History.xlsx',index_col=None)

#Question1
dropped = tutor[(tutor['TutorStatus']=='Dropped')&(tutor['CertDate']>'2018-04-01')]
print('#Question1:Which tutors have a Dropped status and have achieved their certification after 4/01/2018?')
print(dropped)

#question2
today = datetime.today()
match.fillna(today,inplace=True)
difference = match['EndDate']-match['StartDate']
mean1 = difference.mean()
print('#Question2:What is the average length of time a student stayed (or has stayed) in the program? ')
print(mean1)

#question3
tempStudent = pd.merge(match,tutor,on='TutorID')
#print(tempStudent)
tempMatch = tempStudent[(tempStudent['TutorStatus']=='Temp Stop')]
print('#Question3:Identify all students who have been matched in 2018 with a tutor whose status is Temp Stop. ')
mylist3 = tempMatch['StudentID'].tolist()
print(mylist3)

#question4
readScore = pd.merge(tempStudent, student,on='StudentID',how = 'outer')
dropStudent = readScore[(readScore['TutorStatus']=='Dropped')]
mylist4 = dropStudent["ReadScore"].tolist()
print('#Question4:List the Read scores of students who were ever taught by tutors whose status is Dropped.')
print(mylist4)

#question5
tutor_2 = match.groupby(['TutorID'])['StudentID'].count()
dict1 = tutor_2.to_dict()
print('#Question5:List the tutors who taught two or more students.')
for key,value in dict1.items():
    if value >=2:
        print(key,value)

#Question6
allStudent =  pd.merge(match,student, on='StudentID')
studentsAll =pd.merge(allStudent, tutor, on='TutorID')
columns = ['StudentID', 'ReadScore', 'TutorID', 'TutorStatus']
data6 = pd.DataFrame(studentsAll, columns=columns)
print('#Question6')
print(data6)
writer = pd.ExcelWriter("Student_Tutor.xlsx")
data6.to_excel(writer, 'Sheet1')
writer.save()

#Question7
student_Group = readScore.groupby(['StudentGroup'])['TutorID'].count()
print('#Question7:For each student group, list the number of tutors who have been matched with that group.')
print(student_Group)
    
#Question8
readScore['StartDate']=pd.to_datetime(readScore['StartDate'])
readScore['Month']=readScore['StartDate'].dt.month
data8=readScore[(readScore['Month'].isin ([5,6]))&(readScore['EndDate']>='06/30/2018')]
print('#Question8:List all active students who started in May and June. ')
mylist8=data8['StudentID'].values
print(mylist8)

#Question9
allStudent=pd.merge(match,student,how='outer')
print(allStudent)
noTutor=allStudent[allStudent['TutorID'].isnull()]
print('#Question9:Find students who have not been tutored yet. The StudentID is')
mylist9=noTutor['StudentID'].tolist()
print(mylist9)

#Question10
allTutor=pd.merge(match,tutor,how='outer')
print(allTutor)
noStudent=allTutor[allTutor['StudentID'].isnull()]
print('#Question10:Find tutors who did not tutor any students. The TutorID is ')
mylist10=noStudent['TutorID'].tolist()
print(mylist10)


























