# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np

#%% PART 1
results = []
lines = []
with open('input/input10.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for line in file:
        lines.append(list(map(int, list(line.strip()))))            

matrix = np.array(lines)
#%%

def path(position):
    step = matrix[position]
    matrix[position] = 99
    nextStep = step + 1
    rows, cols = matrix.shape
       matrix[position] = step

    
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
   
    valid_indices = []
    for dy, dx in offsets:
        y_new, x_new = position[0] + dy, position[1] + dx
        if 0 <= y_new < rows and 0 <= x_new < cols:
            if matrix[y_new, x_new] == nextStep: 
                valid_indices.append((y_new, x_new))
    if nextStep == 9:
        return valid_indices
    else:
        trail_stops = []
        for newPos in valid_indices:
            trail_stops.extend(path(newPos))
        return set(trail_stops)

zero_indices  = np.where(matrix == 0)
trail_starts = list(zip(zero_indices[0], zero_indices[1]))
trail_heads = []
score = 0
for start in trail_starts:
    trail_heads.append(path(start))
    score += len(trail_heads[-1])

print(trail_heads)
print("final", score)

#%% PART 2

def path(position):
    step = matrix[position]
    matrix[position] = 99
    nextStep = step + 1
    rows, cols = matrix.shape
   
    matrix[position] = step

    
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
   
    valid_indices = []
    for dy, dx in offsets:
        y_new, x_new = position[0] + dy, position[1] + dx
        if 0 <= y_new < rows and 0 <= x_new < cols:
            if matrix[y_new, x_new] == nextStep: 
                valid_indices.append((y_new, x_new))
    if nextStep == 9:
        return valid_indices
    else:
        trail_stops = []
        for newPos in valid_indices:
            trail_stops.extend(path(newPos))
        return trail_stops

zero_indices  = np.where(matrix == 0)
trail_starts = list(zip(zero_indices[0], zero_indices[1]))
trail_heads = []
score = 0
for start in trail_starts:
    trail_heads.append(path(start))
    score += len(trail_heads[-1])

print(trail_heads)
print("final", score)
