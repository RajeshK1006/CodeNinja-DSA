from os import *
from sys import *
from collections import *
from math import *

def findArraySum(a, n, b, m):
    # Write your code here.
    str1 = "".join(map(str,a))
    str2 = "".join(map(str,b))
    ans = int(str1)+int(str2)
    return [i for i in str(ans)]
