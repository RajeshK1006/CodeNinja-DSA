# cook your dish here
import math
def chec(x,y):
    need = abs(x-y)
    if need ==0:
        return 0
    if need <=8:
        return 1  # -*- coding: latin-1 -*
    else:
        return math.ceil(need/8)
    
t = int(input())
for i in range(t):
    x,y =  map(int, input().split())
    print(chec(x,y))
