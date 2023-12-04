# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:10:13 2023

@author: siicn01
"""

import regex as re

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

with open("input\\input3.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# Part 1

# sumOfParts = 0

# symbols = [None] * len(lines)
# partSpaces = [None] * len(lines)

# for x in range(len(lines)):
#     symbols[x] = [m.start(0) for m in re.finditer(r'[^(0123456789.)]', lines[x])]
#     symbols[x] = symbols[x] + [x+1 for x in symbols[x]] + [x-1 for x in symbols[x]]

# for x in range(len(lines)):
#     partSpaces[x] = set()
#     if (x>0 and x<(len(lines)-1)):
#         partSpaces[x].update(symbols[x - 1])
#         partSpaces[x].update(symbols[x])
#         partSpaces[x].update(symbols[x + 1])
#         print(str(x) +  " is between 1 and " + str(len(lines)-1))
#     elif (x == 0):
#         partSpaces[x].update(symbols[x])
#         partSpaces[x].update(symbols[x + 1])
#         print(str(x) +  " is  0")
#     elif(x == (len(lines)-1)):
#         partSpaces[x].update(symbols[x - 1])
#         partSpaces[x].update(symbols[x])
#         print(str(x) +  " is " + str(len(lines)-1))
        
#     matches = [(m.span(), m.group()) for m in re.finditer(r'\d+(?!\d)', lines[x])]
#     for y in range(len(matches)):
#         if (partSpaces[x].intersection(set(range(matches[y][0][0],matches[y][0][1])))):
#             sumOfParts += int(matches[y][1])
 
# print(sumOfParts)

# Part 2
sumOfGears = 0

symbols = [None] * len(lines)
gearsSameLine =  [None] * len(lines)
gearOne = [None] * len(lines)
gearTwo = [None] * len(lines)

for x in range(len(lines)):
    gearsSameLine[x] = re.findall(r'\d+\*\d+', lines[x])
    if(gearsSameLine[x]):
        for y in range(len(gearsSameLine[x])):
            print(gearsSameLine[x][y])
            gearNums = re.findall(r'\d', gearsSameLine[x][y])
            sumOfGears += int(gearNums[0]) * int(gearNums[1])
        print(sumOfGears)
    
    # gearOne[x] = set()
    # gearOne[x] = [m.span() for m in re.finditer(r'\d+(?!\d)', lines[x])]
    # gearOne[x] = gearOne[x] + [x+1 for x in gearOne[x]] + [x-1 for x in gearOne[x]]
    
    # gearTwo[x] = set()
    # gearTwo[x] = [m.span() for m in re.finditer(r'(\*)', lines[x])]
    
    # gearSpaces[x] = set()
    
    # if(gearOne[x].intersection(set(range(matches[y][0][0],matches[y][0][1])))):
    


# for x in range(len(lines)):
#     gearSpaces[x] = set()
#     if (x>0 and x<(len(lines)-1)):
#         gearSpaces[x].update(symbols[x - 1])
#         gearSpaces[x].update(symbols[x])
#         gearSpaces[x].update(symbols[x + 1])
#     elif (x == 0):
#         gearSpaces[x].update(symbols[x])
#         gearSpaces[x].update(symbols[x + 1])
#     elif(x == (len(lines)-1)):
#         gearSpaces[x].update(symbols[x - 1])
#         gearSpaces[x].update(symbols[x])
        
#     matches = [(m.span(), m.group()) for m in re.finditer(r'\d+(?!\d)', lines[x])]
#     for y in range(len(matches)):
#         if (gearSpaces[x].intersection(set(range(matches[y][0][0],matches[y][0][1])))):
#             sumOfGears += int(matches[y][1])
 
# print(sumOfGears)

print(lines[0])
# print([m.span() for m in re.finditer(r'\d+(?!\d)', lines[0])])
# print(lines[0][11])