# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#%% PART 1
lines = []
with open('input/input4.txt', 'r') as file:
    for line in file:
        lines.append(line)

df = matrix = np.array([list(line.strip()) for line in lines])


#%%

def plot_matrix_with_highlight(matrix, highlights=None):
    """
    Plots the input matrix with optional highlighted tiles.

    Args:
    - matrix (np.ndarray): The matrix to be plotted.
    - highlights (list of tuples): A list of tuples (y, x, color) where:
        y, x are the row and column of the tile to highlight.
        color is the background color for the tile.
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')

    rows, cols = matrix.shape

    for y in range(rows):
        for x in range(cols):
            facecolor = "white"
            
            if highlights:
                for hy, hx, color in highlights:
                    if y == hy and x == hx:
                        facecolor = color
            
            rect = plt.Rectangle((x, rows - y - 1), 1, 1, edgecolor='black', facecolor=facecolor)
            ax.add_patch(rect)
            
            ax.text(x + 0.5, rows - y - 0.5, matrix[y, x], ha='center', va='center', fontsize=12)

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.show()

#%%
# Highlight tiles (row, col, color)
highlights = []

xmas_count = 0

for (y, x), value in np.ndenumerate(matrix):
    leftborder = (x >= 3)
    rightborder = (x <= df.shape[1] - 4)
    bottomborder = (y <= df.shape[0] - 4)

    if (leftborder and bottomborder):
        diagonal_left = matrix[y,x] + matrix[y+1,x-1] + matrix[y+2,x-2] + matrix[y+3,x-3]
        if(diagonal_left == "XMAS" or diagonal_left == "SAMX"):
            xmas_count += 1
            # highlights.extend([(y, x, "yellow"), (y+1,x-1, "yellow"), (y+2,x-2, "yellow"), (y+3,x-3, "yellow")])
    
    if (rightborder):
        horizontal = matrix[y,x] + matrix[y,x+1] + matrix[y,x+2] + matrix[y,x+3]
        if(horizontal == "XMAS" or horizontal == "SAMX"):
            xmas_count += 1
            # highlights.extend([(y, x, "yellow"), (y,x+1, "yellow"), (y,x+2, "yellow"), (y,x+3, "yellow")])
    if (bottomborder):
        vertical = matrix[y,x] + matrix[y+1,x] + matrix[y+2,x] + matrix[y+3,x]    
        if(vertical == "XMAS" or vertical == "SAMX"):
            xmas_count += 1
            # highlights.extend([(y, x, "yellow"), (y+1,x, "yellow"), (y+2,x, "yellow"), (y+3,x, "yellow")])
    if (rightborder and bottomborder):
        diagonal_right = matrix[y,x] + matrix[y+1,x+1] + matrix[y+2,x+2] + matrix[y+3,x+3]
        if(diagonal_right == "XMAS" or diagonal_right == "SAMX"):
            xmas_count += 1
            # highlights.extend([(y, x, "yellow"), (y+1,x+1, "yellow"), (y+2,x+2, "yellow"), (y+3,x+3, "yellow")])
       
# plot_matrix_with_highlight(matrix, highlights)

print(xmas_count)


#%% PART 2
lines = []
with open('input/input4.txt', 'r') as file:
    for line in file:
        lines.append(line)

matrix = np.array([list(line.strip()) for line in lines])

#%%
xmas_count = 0

for (y, x), value in np.ndenumerate(matrix):
    leftborder = (x >= 1)
    rightborder = (x <= matrix.shape[1] - 2)
    topborder = (y >= 1)
    bottomborder = (y <= matrix.shape[0] - 2)
    if (leftborder and rightborder and topborder and bottomborder):
        if matrix[y,x] == "A":
            diagonal_a = matrix[y-1,x-1] + matrix[y,x] + matrix[y+1,x+1] 
            diagonal_b = matrix[y-1,x+1] + matrix[y,x] + matrix[y+1,x-1] 
            if((diagonal_a == "MAS" or diagonal_a == "SAM") and 
               (diagonal_b == "MAS" or diagonal_b == "SAM")):
                xmas_count += 1
                

print(xmas_count)