# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np

#%% PART 1
pos = []
vel=[]

with open('input/input14.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for line in file:
            parts = line.strip().split(" ")
            pos.append(list(map(int, parts[0].split("=")[1].split(","))))
            vel.append(list(map(int, parts[1].split("=")[1].split(","))))


# %%
    

from collections import Counter

def create_figure(positions, width=11, height=7):
    grid = np.full((height, width), ".", dtype=object)
    position_counts = Counter(map(tuple, positions))

    for (x, y), count in position_counts.items():
        if 0 <= x < width and 0 <= y < height:
            grid[y, x] = str(count)

    return "\n".join("".join(row) for row in grid)

# %%

def listAdd(a,b):
    return list(map(sum, zip(a, b)))

def counter(pos, xlim, ylim):
    quadrants = [[[], []], [[], []]]
    for p in pos:
        x=-99
        y=-99
        if p[0] < (xlim/2)-0.5:
            x = 0
        elif p[0] >= (xlim/2)+0.5:
            x = 1
        if p[1] < (ylim/2)-0.5:
            y = 0
        elif p[1] >= (ylim/2)+0.5:
            y = 1
        if x>=0 and y>=0:
            quadrants[x][y].append(p)
    # print(quadrants)
    product = 1
    for x in quadrants:
        for y in x:
            product *= len(y)
    return product
# %%


p = pos.copy()
v = vel
ylim = 103
xlim = 101

sec = 0

print(create_figure(p, xlim, ylim))



while sec < 100:
    for i in range(len(v)):
        newP = listAdd(p[i], v[i])
        if newP[0] >= xlim:
            newP[0] -= xlim
        elif newP[0] < 0:
            newP[0] += xlim
        if newP[1] >= ylim:
            newP[1] -= ylim
        elif newP[1] < 0:
            newP[1] += ylim
        p[i] = newP
    sec += 1

print("_")
print(create_figure(p, xlim, ylim))
counter(p, xlim, ylim)
         

# %% PART 2
from scipy.spatial.distance import cdist
def mean_distance(positions):
    distances = cdist(positions, positions, metric='euclidean')
    upper_triangle = distances[np.triu_indices_from(distances, k=1)]
    return np.mean(upper_triangle)

# %%
import matplotlib.pyplot as plt


p = np.array(pos.copy())
v = vel
ylim = 103
xlim = 101

sec = 0

meanDis = []

print(create_figure(p, xlim, ylim))

while sec < 10000:
    for i in range(len(v)):
        # print(i)
        # print(p[i], v[i])
        newP = listAdd(p[i], v[i])
        if newP[0] >= xlim:
            newP[0] -= xlim
        elif newP[0] < 0:
            newP[0] += xlim
        if newP[1] >= ylim:
            newP[1] -= ylim
        elif newP[1] < 0:
            newP[1] += ylim
        p[i] = newP
    meanDis.append(mean_distance(p))
    if(meanDis[-1] < 40):
        print("__________")
        print(create_figure(p, xlim, ylim))
    sec += 1

plt.figure(figsize=(8, 5))
plt.plot(range(len(meanDis)), meanDis, marker='o', linestyle='-', label="Mean Distances")
plt.xlabel("Index")
plt.ylabel("Mean Distance")
plt.title("Mean Distances vs Index")
plt.grid(True)
plt.legend()
plt.show()   
# %%
print(np.argmin(meanDis)+1)
