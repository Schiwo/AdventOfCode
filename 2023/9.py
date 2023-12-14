# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:03:46 2023

@author: morit
"""


import regex as re

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

with open("input\\input9.txt") as f:
# with open("input\\example.txt") as f:
    lines = [line.rstrip('\n') for line in f]
 
hist = []

for line in lines:
    hist.append(changeListDatatype(line.split(" ")))

def predict(h):
    newH =  []
    for i in range(1, len(h)):
        newH.append(h[i] - h[i-1])
    if len(set(newH)) == 1:
        return h[-1] + newH[-1]
    else:
        return h[-1] + predict(newH)

# print(sum([predict(e) for e in hist]))

#Part 2


def predict2(h):
    newH =  []
    for i in range(1, len(h)):
        newH.append(h[i] - h[i-1])
    if len(set(newH)) == 1:
        return h[0] - newH[0]
    else:
        return h[0] - predict2(newH)

print(sum([predict2(e) for e in hist]))

