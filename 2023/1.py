# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:10:13 2023

@author: siicn01
"""

import regex as re

with open("input\\input1.txt") as f:
    lines = [line.rstrip('\n') for line in f]

# Part 1

calValSum = 0

for x in range(len(lines)):
    vals = re.findall(r'\d', lines[x])
    calVal = int(vals[0] + vals[-1])
    # print("Calibration value on line " + str(x) + " is " + str(calVal))
    calValSum += calVal


print("P1: The sum of the calibration values is: "  + str(calValSum))


# Part 2

calValSum = 0

num2words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
             "six": "6", "seven": '7', "eight": '8', "nine": '9', "zero": "0"}

for x in range(len(lines)):
    vals = re.findall(r'([\d]|one|two|three|four|five|six|seven|eight|nine)', lines[x], overlapped=True)

    for v in range(len(vals)):
        if vals[v] in num2words:
            vals[v] = num2words[vals[v]]

    calVal = int(vals[0] + vals[-1])
    # print("Calibration value on line " + str(x) + " is " + str(calVal))
    calValSum += calVal

print("P2: The sum of the calibration values is: "  + str(calValSum))