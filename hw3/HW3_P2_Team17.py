# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 19:52:48 2019

@author: Team 17
"""
### HW3-Problem 2
# Make sure each of the 365 numbers represents one specific date
days = [31,28,31,30,31,30,31,31,30,31,30,31]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Default values
firstIndex = 0
lastIndex = 0
# Input and output files
inputFile = open(r'C:\Users\yingy\Desktop\52 python\hw3\steps.txt','r')
outputFile = open(r'C:\Users\yingy\Desktop\52 python\hw3\Results.txt','w')

outputFile.write('Month    Average    Minimum    Maximum\n')
# Read the data
lines = inputFile.readlines()
lines = list(map(int,lines))
# "For-loop" for calculation:
for x in range(0, 12):
    lastIndex = firstIndex + days[x]
    monthLines = lines[firstIndex:lastIndex]
    Average = float(sum(monthLines)) / max(len(monthLines),1)
    Minimum = min(monthLines)
    Maximum = max(monthLines)
  # Output format  
    outputFile.write(str(months[x]) + '        ' + '{0:.2f}'.format(Average)+\
                     '    ' + str(Minimum) + '        ' + str(Maximum) +'\n')
    firstIndex = lastIndex

inputFile.close()
outputFile.close()