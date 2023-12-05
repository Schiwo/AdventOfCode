# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:10:13 2023

@author: siicn01
"""

import regex as re

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

with open("input\\input2.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# Part 1

sumOfGames = 0

for x in range(len(lines)):
    lines[x] = re.sub(r'(Game [0-9\(\)]+: )', ' ', lines[x])
    red = re.findall(r'(\d+(?= red))', lines[x])
    red = changeListDatatype(red)
    maxRed = max(red)


    green = re.findall(r'(\d+(?= green))', lines[x])
    green = changeListDatatype(green)
    maxGreen = max(green)
    
    blue = re.findall(r'(\d+(?= blue))', lines[x])
    blue = changeListDatatype(blue)
    maxBlue = max(blue)
    
    if(maxRed > 12 or maxGreen > 13 or maxBlue > 14):
        print("Game " + str(x+1) + " is impossible")
        print(maxRed)
        print(maxGreen)
        print(maxBlue)        
        print(lines[x])
    else:
        print("Game " + str(x+1) + " can be played")
        print(lines[x])
        sumOfGames += (x+1)

        
    
print(sumOfGames)


# Part 2

sumOfPowers = 0

for x in range(len(lines)):
    lines[x] = re.sub(r'(Game [0-9\(\)]+: )', ' ', lines[x])
    red = re.findall(r'(\d+(?= red))', lines[x])
    red = changeListDatatype(red)
    maxRed = max(red)


    green = re.findall(r'(\d+(?= green))', lines[x])
    green = changeListDatatype(green)
    maxGreen = max(green)
    
    blue = re.findall(r'(\d+(?= blue))', lines[x])
    blue = changeListDatatype(blue)
    maxBlue = max(blue)
    
    sumOfPowers += (maxRed*maxGreen*maxBlue)
    


        
    
print(sumOfPowers)