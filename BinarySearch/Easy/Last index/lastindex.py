from collections import *
from math import *


n = int(input())
ele = list(map(int,input().split()))
x = int(input())
if x not in ele:
    print(-1)
for i in range(len(ele)-1,-1,-1):
    if ele[i] == x:
        print(i)
        break
        