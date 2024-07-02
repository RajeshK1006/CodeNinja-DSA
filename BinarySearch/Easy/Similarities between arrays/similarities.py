from os import *
from sys import *
from collections import *
from math import *

def findSimilarity(arr1, arr2, n, m):

    # Write your code here.
    setarr1  = set(arr1)
    setarr2 = set(arr2)

    intersection_count = len(setarr1.intersection(setarr2))
    union_count = len(setarr1.union(setarr2))

    return intersection_count, union_count