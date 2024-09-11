# cook your dish here
import math

def check(n):
    return int(math.sqrt(n))

t = int(input())
for i in range(t):
    n = int(input())
    print(check(n))
