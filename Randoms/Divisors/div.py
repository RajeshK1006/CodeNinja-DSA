from typing import List
# from math import *

def printDivisors(n: int) -> List[int]:
    # Write your code here
    result = []
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            result.append(i)
            if n//i!=i:
                result.append(n//i)
    return sorted(result)