from os import *
from sys import *
from collections import *
from math import *

def convertString(str):
    # Write your code here
    ans = list(str.split(" "))
    an = [i[0].upper()+i[1:] if len(i)>1 else i.capitalize() for i in ans ]
    return " ".join(an)