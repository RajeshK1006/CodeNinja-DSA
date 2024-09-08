# cook your dish here
import math
def check(n,x):
    if n<x:
        return 0
    candy = n-x
    
    
    return math.ceil(candy/4)
    
t = int(input())
for i in range(t):
    n,x= map(int,input().split())
    print(check(n,x))
