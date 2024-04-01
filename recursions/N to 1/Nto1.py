from typing import List

def printNos(x: int) -> List[int]:
    # Write your code here
    arr = []
    c = 1
    printrev(arr,x,c)
    return arr

def printrev(st,n,m):
    if n<m:
        return st
    st.append(n)
    n-=1
    printrev(st,n,m)