# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np

#%% PART 1
buttonA = []
buttonB = []
prize = []

with open('input/input13.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for line in file:
        if line.startswith("Button A"):
            # Extract X and Y values for Button A
            x, y = map(int, line.split(':')[1].strip().replace("X+", "").replace("Y+", "").split(", "))
            buttonA.append((x, y))
        elif line.startswith("Button B"):
            # Extract X and Y values for Button B
            x, y = map(int, line.split(':')[1].strip().replace("X+", "").replace("Y+", "").split(", "))
            buttonB.append((-x, -y))
        elif line.startswith("Prize"):
            # Extract X and Y values for Prize
            x, y = map(int, line.split(':')[1].strip().replace("X=", "").replace("Y=", "").split(", "))
            prize.append((x, y))
         

#%%


def intersect(p1, d1, p2, d2):
    p1, d1, p2, d2 = map(np.array, (p1, d1, p2, d2))

    A = np.array([d1, -d2]).T
    b = p2 - p1
    try:
        a, b = np.linalg.solve(A, b)
        a = round(a, 3)
        b = round(b, 3)
        if (a.is_integer() and  b.is_integer()):
            return a, b
        else:
            return 0,0
    except np.linalg.LinAlgError:
        # If lines are parallel or coincident, no unique solution
        return None

totalCosts = 0
for i in range(len(buttonA)):
    minInter = intersect((0,0), buttonA[i], prize[i], buttonB[i])
    machineCosts = 3*minInter[0] + minInter[1]
    totalCosts += machineCosts
print(totalCosts)


# %% Part2

def intersect(p1, d1, p2, d2):
    p1, d1, p2, d2 = map(np.array, (p1, d1, p2, d2))

    A = np.array([d1, -d2]).T
    b = p2 - p1
    try:
        a, b = np.linalg.solve(A, b)
        a = round(a, 3)
        b = round(b, 3)
        if (a.is_integer() and  b.is_integer()):
            return a, b
        else:
            return 0,0
    except np.linalg.LinAlgError:
        # If lines are parallel or coincident, no unique solution
        return None

totalCosts = 0
for i in range(len(buttonA)):
    prize[i]
    minInter = intersect((0,0), 
                         buttonA[i], 
                         (prize[i][0] + 10000000000000, prize[i][1] + 10000000000000), 
                         buttonB[i])
    machineCosts = 3*minInter[0] + minInter[1]
    totalCosts += machineCosts
print(totalCosts)