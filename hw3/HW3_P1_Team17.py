# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:51:39 2019

@author: Team 17
"""
### HW3 Problem-1
# 1. Word counter:
def Word_counter(str1):  
    print(len(str1.split()), "words")

# 2. Average number of letters:
def Average(str1):
    count0=0
    for i in str1:
        if (i.isspace()):       # Spaces
            count0=count0+1
    average=(len(str1)-count0)/len(str1.split())
    print("The average is",'{0:.2f}'.format(average))

# 3. Upper case letters:
def Upper_case_letters(str1):
    count1 = 0
    for i in str1:
        if (i.isupper()):
            count1 = count1 + 1       
    print("There are",count1,"upper case letters in the above string.")

# 4. Lower case letters:
def Lower_case_letters(str1):
    count2 = 0
    for i in str1:
        if (i.islower()):
            count2 = count2 + 1       
    print("There are",count2,"upper case letters in the above string.")

# 5. Reverse the string:
def Reverse(str1):
    print("The reverse string is :",str1[::-1])

# 6. String stats:
def Number_alphabets(str1):
    count3=0
    count4=0
    count5=0
    count6=0
    for i in str1:
        if (i.isalpha()):          # Count alphabets
            count3=count3+1
        elif (i.isdigit()):        # Count digits
            count4=count4+1
        elif (i.isspace()):        # Count spaces
            count5 = count5+1
        else:
            count6=count6+1        # Count characters
    print("There are",count3,"alphabets in the above string.")
    print("There are",count4,"digits in the above string.")
    print("There are",count6,"special characters in the above string.")

# Call all the functions
def main():
    str1=input("Please input a string: ")      # Get input
    Word_counter(str1)
    Average(str1)
    Upper_case_letters(str1)
    Lower_case_letters(str1)
    Reverse(str1)
    Number_alphabets(str1)
main()
###Tweet-1: lets you choose #CleanPower for NO additional cost! IT IS A NO-BRAINER!!!
###Tweet-2: Tesla software V10 is lookin real good! Releasing to early access list soon …