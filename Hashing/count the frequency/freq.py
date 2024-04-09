from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    freq = [0]*n
    for i in edges:
        if 1<=i<=n:
            freq[i-1]+=1
    return freq