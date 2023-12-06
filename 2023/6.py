# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 15:10:19 2023

@author: siicn01
"""

import regex as re
import numpy as np

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

with open("input\\input6.txt") as f:
# with open("input\\example.txt") as f:
    lines = [line.rstrip('\n') for line in f]
    


# Part 1
winHolds = []

times = changeListDatatype(re.findall(r'\d+', re.sub(r'(Time:\s*)', ' ', lines[0])))
distances = changeListDatatype(re.findall(r'\d+', re.sub(r'(Distance:\s*)', ' ', lines[1])))

def distance(t, ht):
    speed = ht
    driveTime = t-ht
    dist = speed * driveTime
    return dist

def winningHolds(time, dist):
    wins = []
    for t in range(time):
        if(distance(time, t) > dist):
            wins.append(t)
    return len(wins)

for ti, di in zip(times, distances):
    winHolds.append(winningHolds(ti, di))
    
print("Part1 result: " + str(np.prod(winHolds)))


# Part 2

newLines = [re.sub((r'\s+'), '', l) for l in lines]

times = changeListDatatype(re.findall(r'\d+', re.sub(r'(Time:\s*)', ' ', newLines[0])))[0]
distances = changeListDatatype(re.findall(r'\d+', re.sub(r'(Distance:\s*)', ' ', newLines[1])))[0]

print("Part2 result: " + str(winningHolds(times, distances)))