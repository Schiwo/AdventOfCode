# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:07:11 2025

@author: morit
"""


#%%
import numpy as np
import copy
with open('input/7.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    lines = file.read().strip().split("\n")
    for i in range(len(lines)):
        lines[i] = list(lines[i])
    
grid = np.array(lines)
for line in grid:
    print(line)
# print(grid)
    
position = (np.where(grid == "S")[0][0],np.where(grid == "S")[1][0])
print(position)

# %% PART 1


def find_split(mat, pos):
    r, c = pos
    n_rows = mat.shape[0]

    # iterate from the next row downward
    for rr in range(r + 1, n_rows):
        if mat[rr, c] == "^":
            return (rr, c)

    return None

def count_splits(mat, start_pos):
    n_rows, n_cols = mat.shape
    visited = set()          
    split_positions = set()  

    queue = [start_pos]
    grido = copy.deepcopy(mat)

    while queue:
        pos = queue.pop(0)

        if pos in visited:
            continue
        visited.add(pos)

        next_pos = find_split(mat, pos)

        if next_pos is None:
            grido[pos[0]:, pos[1]] = "|"
            continue

        grido[pos[0]:next_pos[0], pos[1]] = "|"

        r, c = next_pos
        grido[r][c] = "X"

        split_positions.add(next_pos)

        if c - 1 >= 0:
            new_pos = (r, c - 1)
            if new_pos not in visited:
                queue.append(new_pos)

        if c + 1 < n_cols:
            new_pos = (r, c + 1)
            if new_pos not in visited:
                queue.append(new_pos)

    return len(split_positions)



print(grid)
print("Number of splits: ", count_splits(grid, position))

# %% PART 2

from functools import lru_cache

def count_routes(mat, start_pos):
    n_rows, n_cols = mat.shape

    @lru_cache(maxsize=None)
    def routes_from(pos):
        r, c = pos
        next_pos = find_split(mat, pos)

        if next_pos is None:
            return 1

        rr, cc = next_pos
        total = 0

        if cc - 1 >= 0:
            total += routes_from((rr, cc - 1))

        if cc + 1 < n_cols:
            total += routes_from((rr, cc + 1))

        return total

    return routes_from(start_pos)

print("Number of routes: ", count_routes(grid, position))

