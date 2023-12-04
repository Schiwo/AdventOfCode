# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:10:13 2023

@author: siicn01
"""

import regex as re

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

with open("input\\input4.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# Part 1

# points = 0

# numbers = [None] * len(lines)
# winners = [None] * len(lines)



# for x in range(len(lines)):
#     lines[x] = re.sub(r'(Card\s+[0-9\(\)]+:\s)', ' ', lines[x])
#     lines[x] = re.split(r"\|", lines[x])
#     winners[x] = re.findall(r'\d+', lines[x][0])
#     numbers[x] = re.findall(r'\d+', lines[x][1])
#     winNums = len(set(winners[x]) & set(numbers[x]))
#     if (winNums > 0):
#         points +=  2**(winNums - 1)
    


    
# print(points)


# Part 2
import numpy as np

cards = 0
cardsN = len(lines)

depth = 0

for x in range(cardsN):
    lines[x] = re.sub(r'(Card\s+[0-9\(\)]+:\s)', ' ', lines[x])
    lines[x] = re.split(r"\|", lines[x])
    winners[x] = re.findall(r'\d+', lines[x][0])
    numbers[x] = re.findall(r'\d+', lines[x][1])

def win(cardID):
    depth+=1
    print(depth)
    print("Current Card: " + str(cardID))
    wins = list(range(cardID+1, cardID + 1 + len(set(winners[cardID]) & set(numbers[cardID]))))
    print(wins)
    wins = list(filter(lambda num: num < cardsN, wins))
    if(len(wins) == 0):
        print("no win!")
        return 1
    else:
        return 1 + sum(list(map(win, wins)))
        # return np.product(list(map(win, wins)))
    

cards=win(0)
# for x in range(len(lines)):
#     print(win(x))
    


    
print(cards)