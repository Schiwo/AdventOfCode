# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:07:11 2025

@author: morit
"""


#%%
import numpy as np

with open('input/3.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    lines = file.read().strip().split("\n")
    
banks = lines
print(banks)


# %% PART 1
total = 0

def highest_joltage(s: str) -> int:
    digits = np.array([int(c) for c in s if c.isdigit()])
    
    uniq = np.unique(digits[:-1])
    tens = np.max(uniq)
    
    idxTens = np.where(digits == tens)[0]
    uniq2 = np.unique(digits[idxTens[0]+1:])
    ones = np.max(uniq2)
        
    return tens * 10 + ones


for bank in banks:
    batteryJolt = highest_joltage(bank)
    print(batteryJolt)
    total += batteryJolt

print("Total joltage: ", total)

# %% PART 2

total = 0

def highest_joltage2(s: str) -> int:
    digits = np.array([int(c) for c in s if c.isdigit()])
    
    batteries = []
    jolt = 0

    print(digits)
    for x in range(1, 13):
        if x == 12:
            uniq = np.unique(digits[:])
            # print(digits[idCut:])
            # print(digits)

        else:
            uniq = np.unique(digits[: (x-12)])
            print(digits[:(x-12)])
            # print(x)
            
        maxBattery = np.max(uniq)
        print("max:", maxBattery)
        idCut = np.where(digits == maxBattery)[0][0] + 1
        digits = digits[idCut:]
        batteries.append(maxBattery)

        # print(maxBattery)
        
    jolt = int("".join(str(x) for x in batteries))
    return jolt


for bank in banks[:]:
    batteryJolt = highest_joltage2(bank)
    print(batteryJolt)
    total += batteryJolt

print("Total joltage: ", total)
