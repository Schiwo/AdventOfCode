# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np

#%% PART 1
results = []
lines = []
with open('input/input12.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for line in file:
        lines.append(list(line.strip()))      

matrix = np.array(lines)
#%%

noGo = set()
totalFenceLength = 0

def findRegion(matrix, y,x):
    value = matrix[y, x]
    rows, cols = matrix.shape
    visited = set()
    to_visit = [(y, x)]
    connected_positions = set() 
    fence_positions = []
    
    while to_visit:
        current_y, current_x = to_visit.pop(0)
    
        if (current_y, current_x) in visited:
            continue
    
        visited.add((current_y, current_x))
        connected_positions.add((current_y, current_x))
    
        neighbors = [
            (current_y - 1, current_x),
            (current_y + 1, current_x),
            (current_y, current_x - 1),
            (current_y, current_x + 1)
        ]
    
        for ny, nx in neighbors:
            if (ny, nx) not in visited:
                if 0 <= ny < rows and 0 <= nx < cols and matrix[ny, nx] == value:
                    to_visit.append((ny, nx))
                else:
                    fence_positions.append((ny, nx))
                    
    print(value, len(connected_positions), len(fence_positions))
    fence_length = len(fence_positions) * len(connected_positions)
    return (connected_positions, fence_length)


for (y,x), value  in np.ndenumerate(matrix):
    if (y,x) in noGo:
        continue
    res = findRegion(matrix, y, x)
    region = res[0]
    fence = res[1]
    noGo.update(region)
    totalFenceLength += fence

print(totalFenceLength)

# %% PART2

noGo = set()
totalPrice = 0

def findRegion(matrix, y,x):
    value = matrix[y, x]
    rows, cols = matrix.shape
    visited = set() 
    to_visit = [(y, x)]
    connected_positions = set() 
    fence_positions = []
    fence_corners = 0
    
    while to_visit:
        current_y, current_x = to_visit.pop(0)
    
        if (current_y, current_x) in visited:
            continue
    
        visited.add((current_y, current_x))
        connected_positions.add((current_y, current_x))
    
        neighbors = [
            (current_y - 1, current_x),
            (current_y + 1, current_x),
            (current_y, current_x - 1),
            (current_y, current_x + 1)
        ]
    
        for ny, nx in neighbors:
            if (ny, nx) not in visited:
                if 0 <= ny < rows and 0 <= nx < cols and matrix[ny, nx] == value:
                    to_visit.append((ny, nx))
                else:
                    fence_positions.append((ny, nx))
                    
    outerCorners = 0
    innerCorners = 0

    for i in set(fence_positions):
        if (i[0] + 1, i[1] + 1) in fence_positions:
                if (i[0], i[1] + 1) in connected_positions:
                    print("outerSW", i)
                    outerCorners += 1
                if (i[0]+1, i[1]) in connected_positions:
                    print("outerNE", i)
                    outerCorners += 1
        if (i[0] + 1, i[1] - 1) in fence_positions:
            if (i[0], i[1] - 1) in connected_positions:
                    print("outerSE", i)
                    outerCorners += 1
            if (i[0] + 1, i[1]) in connected_positions:
                    print("outerNW", i)
                    outerCorners += 1
    print("outerCorners", outerCorners)

    
    for i in connected_positions:
        if (i[0] + 1, i[1] + 1) in connected_positions:
                if (i[0], i[1] + 1) in fence_positions and not (i[0]+1, i[1]) in fence_positions:
                    print("innerSW", i)
                    innerCorners += 1
                if (i[0]+1, i[1]) in fence_positions and not (i[0], i[1] + 1) in fence_positions:
                    print("innerNE", i)
                    innerCorners += 1
        if (i[0] + 1, i[1] - 1) in connected_positions:
            if (i[0], i[1] - 1) in fence_positions and not (i[0] + 1, i[1]) in fence_positions:
                    print("innerSE", i)
                    innerCorners += 1
            if (i[0] + 1, i[1]) in fence_positions and not (i[0], i[1] - 1) in fence_positions:
                    print("innerNW", i)
                    innerCorners += 1
    print("innerCorners", innerCorners)
                    
    
    fence_corners = (innerCorners + outerCorners)
        
    fence_length = len(fence_positions) * len(connected_positions)
    fence_price = len(connected_positions) * fence_corners
    return (connected_positions, fence_price)


for (y,x), value  in np.ndenumerate(matrix):
    if (y,x) in noGo:
        continue
    res = findRegion(matrix, y, x)
    region = res[0]
    price = res[1]
    noGo.update(region)
    totalPrice += price

print(totalPrice)

# findRegion(matrix, 0, 0)
