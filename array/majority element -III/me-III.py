from os import *
from sys import *
from collections import *
from math import *

def countTheNumber(arr, n, k):
    # Write your code here.
    l = []
    c = Counter(arr)
    for key , v in c.items():
        if c[key] >= n//k:
            l.append(key)
    return l