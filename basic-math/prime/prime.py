from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
c=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        c+=1
        if n//i!=i:
            c+=1
if c==2:
    print("YES")
else:
    print("NO")