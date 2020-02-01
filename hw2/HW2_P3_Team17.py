# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:15:44 2019

@author: yingy
"""
# inputs (height and weight) and validate them.
def get_input():
    try:
        height=float(input("Please input  your height(in inches): "))
        weight=float(input("Please input  your weight(in pounds): "))
    except:
        print("Please enter only numbers") 
        return -1, -1
    else:
        if height>=0 and weight>=0:
            return height, weight
        else:
            print("height and weight should be positive numbers ")
            return -1, -1
#calculate BMI, and returns BMI.        
def calculate_BMI(height,weight):       
        
    BMI = float((weight*703) / (height**2))
    print ("Your BMI is ",format(BMI, '.2f'))
#To make it clean, keep only 2 digits after decimal
    return BMI
    

#take the BMI value and compute the weight categories    
def calculate_weight_category(BMI):
        
    if BMI<18.5:
        print("You are underweight")
    elif 18.5<=BMI<=25:
        print("You are optimal")
    elif BMI>=25:
        print("You are overweight")
        
def main():
    valid_height,valid_weight = get_input()
    if valid_height >= 0 and valid_weight >= 0:
        BMI = calculate_BMI(valid_height, valid_weight)
        calculate_weight_category(BMI)
    
main()