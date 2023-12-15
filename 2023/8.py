# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:03:46 2023

@author: morit
"""


import regex as re

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

with open("input\\input8.txt") as f:
# with open("input\\example.txt") as f:
    lines = [line.rstrip('\n') for line in f]
 
maps = []
network = {}

for leftRight in lines[0]:
    if leftRight == "L":
        maps.append(0)
    else:
        maps.append(1)
        

del lines[0:2]




for line in lines:
    key = line[0:3] 
    value = (line[7:10], line[12:15])
    network[key] = value

pos = "AAA"
steps = 0

while (pos != "ZZZ"):
    pos = network[pos][maps[steps % len(maps)]]
    steps += 1
    print(pos)
    
print("Results 1: " + str(steps))


#Part 2


pos = []

for key in network:
    if key[-1] == "A":
        pos.append(key)

def loop(start):
    p = start
    s = 0
    hits = [0]
    distances = []
    
    while (True):
        p = network[p][maps[s % len(maps)]]
        if p[-1] == "Z":
            distances.append(s - hits[-1])
            hits.append(s)
        s += 1
        if(s > 100000):
            break
    return distances

dis = [loop(p) for p in pos]
print(dis)
dis =  [d[-1] for d in dis]
print(dis)

from math import gcd
lcm = 1
for d in dis:
    lcm = lcm*d//gcd(lcm, d)
print(lcm)
