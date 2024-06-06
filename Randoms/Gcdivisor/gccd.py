def calcGDC(n:int, m: int) -> int:
    # Write your code here
    # if n<m:
    #     n,m = m,n
    while m!=0:
        n,m = m , n%m
    return n