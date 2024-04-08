from os import *
from sys import *
from collections import *
from math import *


def printPattern(n):
    for i in range(1,n+1):
            print(" "*(n-i)+"*"*((2*i)-1)+" "*(n-i))