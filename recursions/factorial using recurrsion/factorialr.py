from typing import *

def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    arr = [1]
    return fact(arr,n,1,2)
def fact(l,m,factr,mul):
    if factr*mul>m:
        return l
    factr = factr*mul
    l.append(factr)
    return fact(l,m,factr,mul+1)
