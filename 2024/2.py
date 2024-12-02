# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np
import pandas as pd

#%% PART 1

lines = []   

with open('input/input2.txt', 'r') as file:
    for line in file:
        # Split the line into integers and append to the list
        lines.append(list(map(int, line.split())))
#%%

def test(arr):
    if np.all(arr[:-1] <= arr[1:]) or np.all(arr[:-1] >= arr[1:]):
        row_diff = np.abs(np.diff(arr))
        if np.all((row_diff >= 1) & (row_diff <= 3)):
            return 1
    return 0

safe = 0

for line in lines:
    added = 0
    row = np.array(line)
    added += test(row)
    for i in range(len(row)):
        if (added != 0):
            break
        oneSafety = np.delete(row, i)
        print(oneSafety)
        print(test(oneSafety))
        added += test(oneSafety)
 
    safe += added
            
            
