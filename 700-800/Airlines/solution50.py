# cook your dish here
import math
def check(f,p):
    rem = math.ceil(p/100)
    if rem<=f:
        return 0 
    
    return rem - f

t = int(input())
for i in range(t):
    f,p = map(int, input().split())
    print(check(f,p))
