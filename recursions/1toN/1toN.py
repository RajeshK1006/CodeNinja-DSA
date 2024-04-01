from typing import List

def printNos(x: int) -> List[int]: 
    arr = []
    c= 1
    printnum(arr,c,x)
    return arr

def printnum(st,n,y):
    if n>y:
        return st
    st.append(n)
    n+=1
    printnum(st,n,y)