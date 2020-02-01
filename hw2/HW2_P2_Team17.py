# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 01:09:51 2019

@author: yingy
"""

#KE is the kinetic energy
#m is the object’s mass in kilograms
#v is the object’s velocity in meters per second  

#return the amount of kinetic energy that the object has
def kinetic_energy(m,v):
        KE=(1/2)*m*(v**2)
        return KE
    
def main():
    try:
        #asks the user to enter values for mass and velocity
        mass = float(input("Please enter an object's mass(in kilograms): "))
        velocity = float(input("Please enter an object's velocity(in meters per second): "))
    #If the user enters non-digits
    except ValueError:
        print("Please input a number")
    else:
        # calls the kinetic_energy function to get the object’s kinetic energy and print the value
        if mass > 0 and velocity > 0:
            print("KE = ", kinetic_energy(mass, velocity))
        #the user to enter negative numbers
        else:
            print("Both mass and velocity should be positive")
main()
