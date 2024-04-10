from os import *
from sys import *
from collections import *
from math import *

def evenSumTillN(n):
    # Write your code here.
    c = 0
    for i in range(1,n+1):
        if i%2==0:
            c+=i
    return c