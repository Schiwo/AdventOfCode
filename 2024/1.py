# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:27:51 2024

@author: schiltem93
"""

import numpy as np
import pandas as pd

#%% PART 1
df = pd.read_csv('input/input1.txt', sep="\s+", header=None, names=['a', 'b'])

#%%

for col in df.columns:
    df[col] = np.sort(df[col].to_numpy())

#%%

df['distance'] = abs(df['a'] - df['b'])

result1 = df['distance'].sum()


#%% Part2
df = pd.read_csv('input/input1.txt', sep="\s+", header=None, names=['a', 'b'])

#%%
result2 = 0

for x in df['a'].to_numpy():
    result2 += (x * np.count_nonzero(df['b'].to_numpy() == x))

print(result2)