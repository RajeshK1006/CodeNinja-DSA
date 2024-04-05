from os import *
from sys import *
from collections import *
from math import *

def sumOfMaxMin(arr):
    # Write your code here
    arr.sort()
    return arr[0]+arr[-1]