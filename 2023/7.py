# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:03:46 2023

@author: morit
"""


import regex as re

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

with open("input\\input6.txt") as f:
# with open("input\\example.txt") as f:
    lines = [line.rstrip('\n') for line in f]
    
hands = []    
bids = []
handOrder = []
wins = 0



for l in lines:
       l = l.split()
       hands.append([c for c in  l[0]])
       bids.append(int(l[1]))

#Part 1

cards = {"2": 0,
         "3": 1,
         "4": 2,
         "5": 3,
         "6": 4,
         "7": 5,
         "8": 6,
         "9": 7,
         "T": 8,
         "J": 9,
         "Q": 10,
         "K": 11,
         "A": 12
    }

combos = {"highCard": 0,
          "onePair" : 1,
          "twoPairs": 2,
          "threeOfAKind": 3,
          "fullHouse": 4,
          "fourOfAKind": 5,
          "fiveOfAKind": 6}



def handCombo(hand):
    counts = dict((i, hand.count(i)) for i in hand)
    maxC = max(counts.values())
    minC = min(counts.values())
    if(maxC == 5):
        return combos["fiveOfAKind"]
    elif(maxC == 4):
        return combos["fourOfAKind"]
    elif(maxC == 3 and minC == 2):
        return combos["fullHouse"]
    elif(maxC == 3):
        return combos["threeOfAKind"]
    elif(list(counts.values()).count(2) == 2):
        return combos["twoPairs"]
    elif(maxC == 2):
        return combos["onePair"]
    else:
        return combos["highCard"]
        
for h,b in zip(hands, bids):
    handOrder.append((handCombo(h),[cards[x] for x in h], b))
   
handOrder = sorted(handOrder)


for i in range(len(handOrder)):
    wins += handOrder[i][-1] * (i+1)
    
# print(wins)

#Part 2
hands = []    
bids = []
handOrder = []
wins2 = 0



for l in lines:
       l = l.split()
       hands.append([c for c in  l[0]])
       bids.append(int(l[1]))

cards = {"J": 0,
         "2": 1,
         "3": 2,
         "4": 3,
         "5": 4,
         "6": 5,
         "7": 6,
         "8": 7,
         "9": 8,
         "T": 9,
         "Q": 10,
         "K": 11,
         "A": 12
    }

def handComboJ(hand):
    counts = dict((i, hand.count(i)) for i in hand)
    # print(counts)
    jokerC = 0
    if "J" in counts:
        jokerC = counts["J"]
        del counts["J"]
    if(counts):
        maxC = max(counts.values()) + jokerC
        minC = min(counts.values())
    else:
        maxC = jokerC
        minC = jokerC
    if(maxC == 5):
        return combos["fiveOfAKind"]
    elif(maxC == 4):
        return combos["fourOfAKind"]
    elif(maxC == 3 and minC == 2):
        return combos["fullHouse"]
    elif(maxC == 3):
        return combos["threeOfAKind"]
    elif(list(counts.values()).count(2) == 2):
        return combos["twoPairs"]
    elif(maxC == 2):
        return combos["onePair"]
    else:
        return combos["highCard"]
    
       
for h,b in zip(hands, bids):
    handOrder.append((handComboJ(h),[cards[x] for x in h], b))

   
handOrder = sorted(handOrder)  

for i in range(len(handOrder)):
    wins2 += handOrder[i][-1] * (i+1)
    
print(wins2)
