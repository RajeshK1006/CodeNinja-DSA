from os import *
from sys import *
from collections import *
from math import *

def divideByFour(arr):
    for i in range(len(arr)):
        arr[i]//=4
        if arr[i]==0:
            arr[i]=-1
    return arr
    # Write your code here.