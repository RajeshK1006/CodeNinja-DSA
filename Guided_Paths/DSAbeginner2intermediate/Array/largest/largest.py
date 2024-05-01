from sys import *
from collections import *
from math import *

def largestElement(arr, n: int) -> int:

    arr.sort()
    return arr[-1]