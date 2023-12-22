# # # -*- coding: utf-8 -*-
# # """
# # Created on Thu Dec  7 12:03:46 2023

# # @author: morit
# # """


import regex as re
import numpy as np

def changeListDatatype(inputList, dataType=int):
    return list(map(dataType, inputList))

def getIt(lst, start=0):
    return range(start, len(lst))

# with open("input\\input13.txt") as f:
with open("input\\example.txt") as f:
    lines = [line.rstrip('\n') for line in f]
