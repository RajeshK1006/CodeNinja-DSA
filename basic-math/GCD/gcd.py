def calcGDC(n:int, m: int) -> int:
    # Write your code here
    while m!=0:
        n,m = m ,n%m
    return n
    # pass