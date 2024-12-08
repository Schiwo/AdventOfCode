# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np

#%% PART 1
results = []
lines = []
with open('input/input8.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for line in file:
        lines.append(list(line.strip()))

matrix = np.array(lines)
#%%
antenna_val = np.unique(matrix)
antenna_val = np.delete(antenna_val, np.where(antenna_val == "."))
antennas = {value: list() for value in antenna_val}
antennaPos = []


for value in antennas:
    indices = list(map(tuple, np.argwhere(matrix == value)))  # Find indices and convert to set of tuples
    antennaPos.extend(indices)
    antennas[value] = indices

# print(antennaPos)

#%%
antinodes = []

# matrix2 = matrix.copy()

def findAnti(antenna1, antenna2):
    sortedAntennas = sorted([antenna1, antenna2], key=lambda x: x[0])
    antis= []
    antis.append((sortedAntennas[0][0]+(sortedAntennas[0][0]-sortedAntennas[1][0]),
                  sortedAntennas[0][1]+(sortedAntennas[0][1]-sortedAntennas[1][1]))
                 )
    antis.append((sortedAntennas[1][0]+(sortedAntennas[1][0]-sortedAntennas[0][0]),
                  sortedAntennas[1][1]+(sortedAntennas[1][1]-sortedAntennas[0][1]))
                 )
    return antis

for positions in antennas.values(): 
    for i, a in enumerate(positions):
        for b in positions[i+1:]:
            antinodes.extend(findAnti(a, b))
        
antinodes = [node for node in antinodes if (
        all(x >= 0 for x in node) and #left/top boundary
        (node[0] < matrix.shape[0]) and #bottom boundary
        (node[1] < matrix.shape[1]) #and #right boundary
        )
        ]

antinodes = set(antinodes) #use set to remove duplicates

# for x in antinodes:
#     matrix2[x[0], x[1]] = "#"

print(len(antinodes))

# %% PART 2

#%%
antinodes = []

# matrix2 = matrix.copy()

def findAnti2(antenna1, antenna2):
    sortedAntennas = sorted([antenna1, antenna2], key=lambda x: x[0])
    antis= [antenna1, antenna2]
    
    lower = sortedAntennas[0]
    upper = sortedAntennas[1]
    lowerStepY = lower[0]-upper[0]
    lowerStepX = lower[1]-upper[1]
    
    upperStepY = upper[0]-lower[0]
    upperStepX = upper[1]-lower[1]
    
    while True:
        breakc = 0       
        lower = (lower[0]+lowerStepY,lower[1]+lowerStepX)
        upper = (upper[0]+upperStepY, upper[1]+upperStepX)
        if (all(x >= 0 for x in lower) and 
        (lower[0] < matrix.shape[0]) and #bottom boundary
        (lower[1] < matrix.shape[1]) #and #right boundary
        ):
            antis.append(lower)
        else:
            breakc += 1
        if (all(x >= 0 for x in upper) and 
        (upper[0] < matrix.shape[0]) and #bottom boundary
        (upper[1] < matrix.shape[1]) #and #right boundary
        ):
            antis.append(upper)
        else:
            breakc += 1
        if breakc >=2:
            break
    return antis

for positions in antennas.values(): 
    for i, a in enumerate(positions):
        for b in positions[i+1:]:
            antinodes.extend(findAnti2(a, b))
        
antinodes = [node for node in antinodes if (
        all(x >= 0 for x in node) and #left/top boundary
        (node[0] < matrix.shape[0]) and #bottom boundary
        (node[1] < matrix.shape[1]) #and #right boundary
        )
        ]

antinodes = set(antinodes) #use set to remove duplicates

# for x in antinodes:
#     matrix2[x[0], x[1]] = "#"

print(len(antinodes))


