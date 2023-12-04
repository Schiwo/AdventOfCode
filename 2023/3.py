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
import numpy as np
from itertools import product


def find_true_indices(lst, index=0):
    print(lst)
    if index >= len(lst):
        return []
    elif lst[index]:
        return [index] + find_true_indices(lst, index+1)
    else:
        return find_true_indices(lst, index+1)

sumOfGears = 0

symbols = [None] * len(lines)
gearsSameLine =  [None] * len(lines)
gearsNum = [None] * len(lines)
gearsNumId = [None] * len(lines)
gearsMiddle = [None] * len(lines)


for x in range(len(lines)):
   
    gearsNum[x] = [m.group() for m in re.finditer(r'\d+(?!\d)', lines[x])]
    gearsNumId[x] = [[range(m.span()[0], m.span()[1])] for m in re.finditer(r'\d+(?!\d)', lines[x])]


    if (x>0):
        gearsNum[x].extend([m.group() for m in re.finditer(r'\d+(?!\d)', lines[x-1])])
        gearsNumId[x].extend([[range(m.span()[0], m.span()[1])] for m in re.finditer(r'\d+(?!\d)', lines[x-1])])
    if (x < (len(lines)-1)):
        gearsNum[x].extend([m.group() for m in re.finditer(r'\d+(?!\d)', lines[x+1])])
        gearsNumId[x].extend([[range(m.span()[0], m.span()[1])] for m in re.finditer(r'\d+(?!\d)', lines[x+1])])
        
    gearsMiddle[x] = [m.start(0) for m in re.finditer(r'\*', lines[x])]
    
    for g in gearsMiddle[x]:
        adjacentNums = []
        for n in range(len(gearsNumId[x])):
            if(np.isclose(g, gearsNumId[x][n], rtol = 0, atol = 1).any()):
                adjacentNums.append(int(gearsNum[x][n]))
        if(len(adjacentNums) == 2):
            sumOfGears += np.product(adjacentNums)


print(sumOfGears)
     