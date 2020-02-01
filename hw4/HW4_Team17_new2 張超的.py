# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:44:15 2019

@author: Team 17
"""
## HW4
# Open the file WorldSeriesWinners.txt and read the data
File=open(r"C:/Users/yingy/Desktop/52 python/hw4/WorldSeriesWinners.txt","r")
Team=[]     # the list of teams
for line in File:
    Team.append(line.strip())
    
# Creat the list of year  
Year=[]
for i in range(1903,2010):
    if i == 1904 or i== 1994:    # skip 1904 and 1994
        continue
    Year.append(i)

# Store the team names in a dictionary    
winList={}    
for i in range(len(Year)):
    winList[Year[i]]=Team[i]

# Create the first dictionary, winYear, in which keys are the team names
# and values are a list of the winning years 
winYear={}
for Year, name in winList.items():
    if name not in winYear:
        winYear[name]=[]
    winYear[name].append(Year)
print("\nThe dictionary of teams and win years\n")
print(winYear,"\n")

# Display the teams 
print("Team :             win years ")
for name in winYear.keys():
    print(name, ":", winYear[name])
    
# Create the second dictionary, total_wins, to count the total #of wins
print("\nTeam", "\t"*2, "Number of wins")
total_wins={}
for name, Year in winYear.items():
    print(name, "  ", len(Year))
# Sort this dictionary and display the "stars"
win_rank=[]
for name, Year in winYear.items():
    Team=(len(Year), name)
    win_rank.append(Team)
win_rank.sort(reverse=True)

print("\nTeam (number of wins)   Stars")    
for i in range(len(win_rank)):
    print(win_rank[i][1],"(", win_rank[i][0],")", "*"*win_rank[i][0])