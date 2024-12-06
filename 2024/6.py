# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np
import pandas as pd

#%% PART 1
lines = []
with open('input/input6.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    for line in file:
        lines.append(list(line.strip()))
        
startMatrix = np.array(lines)
#%%
startMatrix = np.array(lines)
startdir = "^"
startY=np.argwhere(startMatrix == "^")[0][0]
startX=np.argwhere(startMatrix == "^")[0][1]


def move(y, x, direction, matrix):
    if (direction == "^"):
        if "#" in matrix[:y, x]:
            newY = max(np.argwhere(matrix[:y, x] == "#"))[0] + 1
            newDir = ">"
            matrix[newY:y+1, x] = "X"
            return move(newY, x, newDir, matrix)
        else:
            matrix[:y, x] = "X"
            return matrix
    if (direction == ">"):
        if "#" in matrix[y, x:]:
            newX = x+min(np.argwhere(matrix[y, x:] == "#"))[0] - 1
            newDir = "v"
            matrix[y, x:newX+1] = "X"
            return move(y, newX, newDir, matrix)
        else:
            matrix[y, x:] = "X"
            return matrix
    if (direction == "v"):
        if "#" in matrix[y:, x]:
            newY = y+min(np.argwhere(matrix[y:, x] == "#"))[0] - 1
            newDir = "<"
            matrix[y:newY+1, x] = "X"
            return move(newY, x, newDir, matrix)
        else:
            matrix[y:, x] = "X"
            return matrix
    if (direction == "<"):
        if "#" in matrix[y, :x]:
            newX = max(np.argwhere(matrix[y, :x] == "#"))[0] + 1
            newDir = "^"
            matrix[y, newX:x+1] = "X"
            return move(y, newX, newDir, matrix)
        else:
            matrix[y, :x] = "X"
            return matrix
        

final_matrix = move(startY, startX, startdir, startMatrix)
print(final_matrix)
print(np.count_nonzero(final_matrix == "X"))

#%%

def count_loops(final_matrix, startY, startX, startdir):
    def simulate_move(y, x, direction, matrix):
        visited_positions = set()
        while True:
            if (y, x, direction) in visited_positions:
                return True  # Loop detected
            visited_positions.add((y, x, direction))
            
            if direction == "^":
                if "#" in matrix[:y, x]:
                    newY = max(np.argwhere(matrix[:y, x] == "#"))[0] + 1
                    direction = ">"
                    matrix[newY:y+1, x] = "X"
                    y = newY
                else:
                    matrix[:y, x] = "X"
                    break
            elif direction == ">":
                if "#" in matrix[y, x:]:
                    newX = x + min(np.argwhere(matrix[y, x:] == "#"))[0] - 1
                    direction = "v"
                    matrix[y, x:newX+1] = "X"
                    x = newX
                else:
                    matrix[y, x:] = "X"
                    break
            elif direction == "v":
                if "#" in matrix[y:, x]:
                    newY = y + min(np.argwhere(matrix[y:, x] == "#"))[0] - 1
                    direction = "<"
                    matrix[y:newY+1, x] = "X"
                    y = newY
                else:
                    matrix[y:, x] = "X"
                    break
            elif direction == "<":
                if "#" in matrix[y, :x]:
                    newX = max(np.argwhere(matrix[y, :x] == "#"))[0] + 1
                    direction = "^"
                    matrix[y, newX:x+1] = "X"
                    x = newX
                else:
                    matrix[y, :x] = "X"
                    break
        return False  

    loop_count = 0

    for y, x in np.argwhere(final_matrix == "X"):
        test_matrix = final_matrix.copy()
        test_matrix[y, x] = "#"
        
        if simulate_move(startY, startX, startdir, test_matrix):
            loop_count += 1

    return loop_count

total_loops = count_loops(final_matrix, startY, startX, startdir)
print(total_loops)

