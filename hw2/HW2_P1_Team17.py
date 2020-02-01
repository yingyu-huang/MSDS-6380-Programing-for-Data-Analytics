# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 23:34:44 2019

@author: yingy
"""
#check if input number is valid
def validate_input(input_number):
    try:
        score=float(input_number)
    except:
        print("Please enter only numbers") 
    else:
        if 0 <= score <= 100:
            return score
        else:
            print("Score should be between 0.0 and 100.0")

#computes the grade in the score-to-grade mapping table         
def calculate_grade(score):
    
        if score>=90:
            print("A Grade")
        elif score>=80:
            print("B Grade")
        elif score>=70:
            print("C Grade")
        elif score>=60:
            print("D Grade")
        else:
            print("F Grade")

def main():
#Make sure input score is valid, then send the number to calculate_grade() function
    valid_score = validate_input(input("Please enter a score: "))
    if valid_score is not None:
        calculate_grade(valid_score)
        
main()