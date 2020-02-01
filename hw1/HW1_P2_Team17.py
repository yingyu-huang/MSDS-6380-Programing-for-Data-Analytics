# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 16:50:27 2019

@author: Team 17
"""

##Problem 2
# A is the amount of money in the account after the specified number of years.
# P is the principal amount that was originally deposited into the account.
# r is the annual interest rate.
# n is the number of times per year that the interest is compounded.
# t is the specified number of years.
# formula for the balance of the account after a specified number of years is:A = P(1+ (r/n))^(nt)


P = float(input("The amount of principal originally deposited: "))
r = float(input("The annual interest rate: "))
n = int(input(
        "The number of times per year that the interest is compounded: "))
t = int(input("The number of years: "))
A = float(P*(1+ (r/n))**(n*t))
print("The amount of money that will be in the account:", A)