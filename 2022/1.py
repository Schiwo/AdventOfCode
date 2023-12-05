# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:07:50 2022

@author: morit
"""
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)



file1 = open('1.txt', 'r')
lines = file1.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')


sums = []

curSum = 0

for i in range(len(lines)):
    if  lines[i]:
        curSum = curSum + int(lines[i])
    else:
        sums.append(curSum)
        curSum = 0

from numpy import argmax

elf = argmax(sums)

print(elf)
print(sums[elf])

elves = []

for i in range(3):
    elves.append(max(sums))
    sums.remove(max(sums))

print(sum(elves))