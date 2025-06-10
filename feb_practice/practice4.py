# Pandas panel

import pandas as pd
import numpy as np
import random

def fah(tem):
    return ((float(9)/5) * tem + 32)
def cel(tem):
    return (float(5)/9) * (tem - 32)
temp = [15.8, 25, 30.5, 25]


F = list(map(fah, temp))

C = list(map(cel, temp))
print(F)
print(C)