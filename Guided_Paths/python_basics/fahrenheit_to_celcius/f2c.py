from os import *
from sys import *
from collections import *
from math import *

#Your code goes here
s = int(input())
e = int(input())
w = int(input())

for i in range(s,e+1,w):
    c = (i-32)*(5/9)
    if c>=0:
        c=floor(c)
    else:
        c = ceil(c)

    print(i, end=" ")
    print(c)