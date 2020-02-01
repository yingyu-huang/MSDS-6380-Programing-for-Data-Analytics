# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:07:53 2019

@author: yingy
"""
import numpy as np
# Load and prepare the data for analysis
data= np.loadtxt('C:/Users/yingy/Desktop/52 python/hw5/insurance.txt',dtype='str')
data = np.array(data[1:,:])
mywork= np.array([["Result       ","Mean","std","Median"]])  ## Start preparing the output

#1.	Mean, standard deviation and median of age
age=data[:,0]
age=age.astype('int')
mean_age=round(np.mean(age),2)
sd_age=round(np.std(age),2)
median_age=np.median(age)
mywork=np.append(mywork,[['Age          ',mean_age,sd_age,median_age]],axis=0)
#2.	Mean, standard deviation and median of BMI
bmi=data[:,2]
bmi=bmi.astype('float')
mean_bmi=round(np.mean(bmi),2)
sd_bmi=round(np.std(bmi),2)
median_bmi=np.median(bmi)
mywork=np.append(mywork,[['BMI          ',mean_bmi,sd_bmi,median_bmi]],axis=0)
#3.	Mean, standard deviation and median of BMI grouped by sex.
sex=data[:,1]
male_bmi=bmi[sex=='male']
mean_male_bmi=round(np.mean(male_bmi),2)
sd_male_bmi=round(np.std(male_bmi),2)
median_male_bmi=np.median(male_bmi)
mywork=np.append(mywork,[['BMI_Male     ',mean_male_bmi,sd_male_bmi,median_male_bmi]],axis=0)


female_bmi=bmi[sex=='female']
mean_female_bmi=round(np.mean(female_bmi),2)
sd_female_bmi=round(np.std(female_bmi),2)
median_female_bmi=np.median(female_bmi)
mywork=np.append(mywork,[['BMI_Female   ',mean_female_bmi,sd_female_bmi,median_female_bmi]],axis=0)
#4.	Mean, standard deviation and median of BMI for smokers and non-smokers. 
smoker=data[:,4]
smokers_bmi=bmi[smoker=='yes']
mean_smokers_bmi=round(np.mean(smokers_bmi),2)
sd_smokers_bmi=round(np.std(smokers_bmi),2)
median_smokers_bmi=np.median(smokers_bmi)
mywork=np.append(mywork,[['BMI_smoker   ',mean_smokers_bmi,sd_smokers_bmi,median_smokers_bmi]],axis=0)

non_smokers_bmi=bmi[smoker=='no']
mean_non_smokers_bmi=round(np.mean(non_smokers_bmi),2)
sd_non_smokers_bmi=round(np.std(non_smokers_bmi),2)
median_non_smokers_bmi=np.median(non_smokers_bmi)
mywork=np.append(mywork,[['BMI_nonsmoker',mean_non_smokers_bmi,sd_non_smokers_bmi,median_non_smokers_bmi]],axis=0)
#5.	Mean, standard deviation and median of BMI grouped by region
region=data[:,5]
sw_bmi=bmi[region=='southwest']
mean_sw_bmi=round(np.mean(sw_bmi),2)
sd_sw_bmi=round(np.std(sw_bmi),2)
median_sw_bmi=np.median(sw_bmi)
mywork=np.append(mywork,[['BMI_SW       ',mean_sw_bmi,sd_sw_bmi,median_sw_bmi]],axis=0)

se_bmi=bmi[region=='southeast']
mean_se_bmi=round(np.mean(se_bmi),2)
sd_se_bmi=round(np.std(se_bmi),2)
median_se_bmi=np.median(se_bmi)
mywork=np.append(mywork,[['BMI_SE       ',mean_se_bmi,sd_se_bmi,median_se_bmi]],axis=0)

nw_bmi=bmi[region=='northwest']
mean_nw_bmi=round(np.mean(nw_bmi),2)
sd_nw_bmi=round(np.std(nw_bmi),2)
median_nw_bmi=np.median(nw_bmi)
mywork=np.append(mywork,[['BMI_NW       ',mean_nw_bmi,sd_nw_bmi,median_nw_bmi]],axis=0)

ne_bmi=bmi[region=='northeast']
mean_ne_bmi=round(np.mean(ne_bmi),2)
sd_ne_bmi=round(np.std(ne_bmi),2)
median_ne_bmi=np.median(ne_bmi)
mywork=np.append(mywork,[['BMI_NE       ',mean_ne_bmi,sd_ne_bmi,median_ne_bmi]],axis=0)
#6.	Mean, standard deviation and median of BMI of those who have more than 2 children.
children=data[:,3]
children=children.astype('int')
children_bmi=bmi[children>2]
mean_children_bmi=round(np.mean(children_bmi),2)
sd_children_bmi=round(np.std(children_bmi),2)
median_children_bmi=np.median(children_bmi)
mywork=np.append(mywork,[['BMI_kids>2   ',mean_children_bmi,sd_children_bmi,median_children_bmi]],axis=0)

#comments for factors that affect BMI
e1='''Effect of smoking on BMI:  
  The overall average BMI is 30.67. 
  The BMI for non-smokers and smokers are 30.65 and 30.71, respectively. 
  Since the BMI for smokers is slightly higher than for non-smokers, 
  we can conclude that, though not significantly, 
  smokers tend to have a higher value of BMI, than non-smokers. '''
e2='''Effect of Region on BMI: 
   The region of southeast, has a somehow 'significantly' higher mean and median in comparison to all the other three regions. 
   This implies that region does affect BMI values on people.'''
e3='''Effect of more than 2 children on BMI: 
  Mean and median BMI for people with more than two children does not differ significantly from the overall mean and median BMI. 
  So, we conclude that number of children has little effect on people's BMI. '''

 
#sort the data by expense
expense=data[:,6]
expense=expense.astype('float')
c=np.argsort(-expense)
data=data[c]
len(expense)*0.2 #267.6~268
#compute the mean, and standard deviation of BMI 
data20=data[:268,:]   
bmi20=data20[:,2].astype(float)
mean20=round(np.mean(bmi20),2)
sd20=round(np.std(bmi20),2)
mean20,sd20     #32.23, 5.72
#mode of smoker
count1=np.sum(data20[:,4]=='yes')
count2=np.sum(data20[:,4]=='no')
count1,count2  #208, 60
#mode of region
region20_sw=np.sum(data20[:,5]=='southwest')
region20_nw=np.sum(data20[:,5]=='northwest')
region20_se=np.sum(data20[:,5]=='southeast')
region20_ne=np.sum(data20[:,5]=='northeast')
region20_sw,region20_nw,region20_se,region20_ne  #54, 59, 88, 67

e4='''The mean BMI of top 20% of population is 32.23 The sd of BMI for top 20% of population is 5.72
      The mode of top 20% expense for smoking status is 'yes', which is  208
      The mode of top 20% expense for region is 'southeast', which is  88'''

#bottom 80%
data80=data[268:,:]
bmi80=data80[:,2].astype(float)
mean80=round(np.mean(bmi80),2)
sd80=round(np.std(bmi80),2)
mean80,sd80   #30.27, 6.13
#mode of smoker
count3=np.sum(data80[:,4]=='yes')
count4=np.sum(data80[:,4]=='no')
count3,count4    #66, 1004
#mode of region
region80_sw=np.sum(data80[:,5]=='southwest')
region80_nw=np.sum(data80[:,5]=='northwest')
region80_se=np.sum(data80[:,5]=='southeast')
region80_ne=np.sum(data80[:,5]=='northeast')
region80_sw,region80_nw,region80_se,region80_ne #271, 266, 276, 257

#values of the rest 80% of the population
e5='''The mean BMI of the bottom 80% of the population is  30.27 The sd of BMI for the bottom 80% of the population  is 6.13
      The mode of the rest 80% expense for smoking status is 'no', which is  1004
      The mode of the rest 80% expense for region is 'southeast', which is  276'''
      
#the primary reasons for the top 20% of the expenses     
e6='''Primary reasons for top 20% expenses: 
      The people in the top 20% of expenses have a significantly higher mean BMI value compared to the rest 80% of the population(32.23 vs 30.27). 
      And the number of smokers is clearly greater than that of non-smokers among the insurers within the top 20% of expenses(208 vs 60). 
      It is widely known that, high BMI values and being a smoker tend to lead to higher expenses on medical insurance.
      For the residing region, it seems that southeast has the largest population because the modes of both top 20% and the rest 80% are 'southeast' in this sample. 
      Among the top 20%, 88/268 = 32.84%, which is significantly higher than (88+276)/1338 = 27.20% (the overall proportion). 
      Thus, people living in the southeast region tend to have more expenses on insurance, somehow. 
      Anyway, to make a scientific conclusion, further statistical tests are necessary.'''


np.savetxt('C:/Users/yingy/Desktop/52 python/hw5/result_HW5.txt',(mywork,e1,e2,e3,e4,e5,e6),fmt="%-20s")
