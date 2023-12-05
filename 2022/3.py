# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:29:07 2022

@author: morit
"""
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)



file = open('3.txt', 'r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')


leftSide = []
rightSide = []
doubles = []

for i in range(len(lines)):
    leftSide.append(lines[i][:int(len(lines[i])/2)])
    rightSide.append(lines[i][int(len(lines[i])/2):])
    doubles.append(list(set(leftSide[i]).intersection(set(rightSide[i])))[0])


def score(letters):
    x = 0
    for i in range(0, len(letters)):
        upperScore = letters[i].upper()
        if letters[i] == upperScore:
            x += ord(letters[i]) - 38
        else:
            x += ord(letters[i]) - 96
    print("test")
    print(x)
    return x
        
scoreOne = score(doubles)


groups = []
badges = []

for i in range(int(len(lines)/3)):
    groups.append(["","",""])
    for x in range(3):
        groups[i][x] = lines[(i*3)+x]
        
    badges.append(list(set(groups[i][0]).intersection(set(groups[i][1]), set(groups[i][2])))[0])


scoreTwo = score(badges)