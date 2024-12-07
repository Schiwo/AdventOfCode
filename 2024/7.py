# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np
import pandas as pd

#%% PART 1
results = []
lines = []
with open('input/input7.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for line in file:
        lines.append(list(map(int, line.split(":")[1].strip().split())))
        results.append(int(line.split(":")[0].strip()))

print(results)
print(lines)
#%%
def operation(result, total, numbers):
    # print(total)
    # print(numbers)
    if not numbers:
        return total == result
    current = numbers[0]
    remaining = numbers[1:]
    
    if operation(result, total * current, remaining):
        return True
    
    if operation(result, total + current, remaining):
        return True
    
    return False


#%%
calibrations = 0
for i in range(len(lines)):
    if(operation(results[i], lines[i][0], lines[i][1:])):
        calibrations += results[i]    
    # print(results[i])
    # print(lines[i])
    # print(operation(results[i], lines[i][0], lines[i][1:]))

print(calibrations)
   
#%% PART 2

def operation2(result, total, numbers):
    # print(total)
    # print(numbers)
    if not numbers:
        return total == result
    current = numbers[0]
    remaining = numbers[1:]
    
    if operation2(result, total * current, remaining):
        return True
    
    if operation2(result, total + current, remaining):
        return True
    
    if operation2(result, int(str(total) + str(current)), remaining):
        return True
    
    return False


#%%
calibrations = 0
for i in range(len(lines)):
    if(operation2(results[i], lines[i][0], lines[i][1:])):
        calibrations += results[i]    

print(calibrations)

    
