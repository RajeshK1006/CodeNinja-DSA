# cook your dish here
import math 

def check(n,x,y):
    return math.ceil(n/(x*y))

t = int(input())
for i in range(t):
    n,x,y = map(int, input().split())
    print(check(n,x,y))
