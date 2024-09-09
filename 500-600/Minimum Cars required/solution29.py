# cook your dish here
import math
def check(n):
    
    ans = n/4
    return math.ceil(ans)

t = int(input())
for i in range(t):
    n = int(input())
    print(check(n))
