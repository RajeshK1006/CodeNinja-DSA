from os import *
from sys import *
from collections import *
from math import *

def convertString(str):
    # Write your code here
    llist = []
    for i in str.split():
        first = i[0].upper()
        rem = i[1:]
        total = first+rem
        llist.append(total)
    return " ".join(llist)

