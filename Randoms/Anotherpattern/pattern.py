from os import *
from sys import *
from collections import *
from math import *

def ninjaPuzzle(n):

    for i in range(n):
        print(" "*i+"*"*(n-i))