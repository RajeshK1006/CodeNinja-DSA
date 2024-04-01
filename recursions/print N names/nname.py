from  typing import *

def printNtimes(n: int) -> List[str]:
    arr = []
    c = 0
    printstr(arr,c,n)
    return arr

def printstr(st,x,y):
    if x==y:
        return st
    x+=1
    st.append("Coding Ninjas")
    # c+=1
    printstr(st,x,y)