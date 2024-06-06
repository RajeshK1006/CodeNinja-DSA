def isPowerOfTwo(n:int) -> bool:
    # Write your code here
    if n<=0:
        return False
    return n & (n-1) ==0