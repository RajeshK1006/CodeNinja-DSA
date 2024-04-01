from typing import List

def sumFirstN(n: int) -> int:
    # Write your code here.
    summ = 0
    count = 1
    return printsum(n,summ,count)
    
    

def printsum(x,y,z):
    if z>x:
        return y
    y+=z
    z+=1
    return printsum(x,y,z)