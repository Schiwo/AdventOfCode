# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 10:07:11 2025

@author: morit
"""


#%%
import numpy as np

matrix = []
operator = []


# with open('input/6.txt', 'r') as file:
with open('input/example.txt', 'r') as file:
    for line in file:
            stripped = line.strip()
            if not stripped:
                continue
            if not all(token.isdigit() for token in stripped.split()):
                operator = stripped.split()
                continue
            matrix.append([int(x) for x in stripped.split()])
    matrix = np.array(matrix)

print(matrix)


# %% PART 1


def apply_operator(arr, operator):
    if operator == "+":
        return np.sum(arr, dtype=np.int64)
    elif operator == "*":
        return np.prod(arr, dtype=np.int64)
    else:
        raise ValueError(f"Unsupported operator: {operator}")

def result_sum(matrix, operator):
    ressum = 0
    for i in range(matrix.shape[1]):
        result = apply_operator(matrix[:, i], operator[i])
        ressum += result
    return ressum

print("Sum of results: ", result_sum(matrix, operator))

# %% PART 2

import numpy as np

matrix = []
operator = []

def no_whitespace(matrix: np.ndarray) -> np.ndarray:
    mat = matrix.copy()
    n_rows, n_cols = mat.shape

    for j in range(n_cols):
        while all(cell and cell[0] == " " for cell in mat[:, j]):
            for i in range(n_rows):
                mat[i, j] = mat[i, j][1:]

        while all(cell and cell[-1] == " " for cell in mat[:, j]):
            for i in range(n_rows):
                mat[i, j] = mat[i, j][:-1]

    return mat


with open('input/6.txt', 'r') as file:
# with open('input/example.txt', 'r') as file:
    lines = [line.rstrip("\n") for line in file if line.strip()]

    *num_lines, op_line = lines

    col_starts = [i for i, ch in enumerate(op_line) if not ch.isspace()]
    col_starts.append(len(op_line))  # sentinel for last slice

    col_slices = [(col_starts[i], col_starts[i+1]) for i in range(len(col_starts) - 1)]

    matrix_rows = []
    for line in num_lines:
        if len(line) < len(op_line):
            line = line + " " * (len(op_line) - len(line))
        cells = [line[start:end] for (start, end) in col_slices]
        matrix_rows.append(cells)

    ops = []
    if op_line:
        ops = op_line.split()

    matrix = np.array(matrix_rows, dtype=str)
    operator = np.array(ops)

matrix = no_whitespace(matrix)
print(matrix)

# print(operator)
# %% 

def transform_matrix(mat):
    n_rows, n_cols = mat.shape

    result = []

    for j in range(n_cols):
        col = mat[:, j]
        max_len = len(col[0])
        col_result = []

        for digit_index in range(max_len):
            digits = []
            for val in col:
                if digit_index < len(val):
                    digits.append(val[digit_index])

            col_result.append(int("".join(digits)))
        if(len(col_result) < 3):
            print(j)
            print(col_result)
        result.append(col_result)

    return result

def result_sum2(matrix, operator):
    ressum = 0
    for i in range(len(matrix)):
        result = apply_operator(matrix[i], operator[i])
        ressum += result
    return ressum

transformed_matrix = transform_matrix(matrix[:]) 
print("Sum of results: ", result_sum2(transformed_matrix, operator))


