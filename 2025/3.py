# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:07:11 2025

@author: morit
"""


#%%
import numpy as np

with open('input/4.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    lines = file.read().strip().split("\n")
    
grid = lines
print(grid)


# %% PART 1
def count_adjacent_at(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Directions for adjacency (8 neighbors)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    result = []

    for r in range(rows):
        row_results = []
        for c in range(cols):
            if(grid[r][c] != "@"):
                row_results.append(False)
            else:
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # stay inside bounds
                    if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
                        if grid[nr][nc] == "@":
                            count += 1
                if(count < 4):
                    row_results.append(True)
                else:
                    row_results.append(False)
        result.append(row_results)


    
    return result

movable = count_adjacent_at(grid)
count = 0

for row in movable:
    count += row.count(True)

print(count_adjacent_at(grid))
print("Total rolls: ", count)

# %% PART 2

def remove_rolls(grid, mask):

    result = []
    for r in range(len(grid)):
        row = grid[r]
        new_chars = []
        for c in range(len(row)):
            if mask[r][c]:
                new_chars.append(".")
            else:
                new_chars.append(row[c])
        result.append("".join(new_chars))
    return result

for row in grid:
    print(row)

count = 0
while(True):
    removed = 0
    movable = count_adjacent_at(grid)
    grid = remove_rolls(grid, movable)
    for row in movable:
        removed += row.count(True)
    count += removed
    if(removed == 0):
        break
    
print("Total rolls: ", count)

