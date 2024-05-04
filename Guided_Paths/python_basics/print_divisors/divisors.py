from typing import List

def printDivisors(n: int) -> List[int]:
    # Write your code here
    l = []
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            l.append(i)
            if n//i!=i:
                l.append(n//i)
    return sorted(l)