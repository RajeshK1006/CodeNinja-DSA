from os import *
from sys import *
from collections import *
from math import *

def findGcd(x, y):
    # Write your code here
    # Return an integer
    while y!=0:
        x,y = y,x%y
    return x