from os import *
from sys import *
from collections import *
from math import *

n = int(input())
p = len(str(n))
s = 0
for i in str(n):
    e = int(i)**p
    s+=e
    
if n==s:
    print("true")
else:
    print("false")