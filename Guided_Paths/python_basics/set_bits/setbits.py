from os import *
from sys import *
from collections import *
from math import *




#Write your countBits function here.
def countBits(n):
    binary = str(bin(n))
    c= 0
    for i in binary[2:]:
        if int(i)==1:
            c+=1
    return c

