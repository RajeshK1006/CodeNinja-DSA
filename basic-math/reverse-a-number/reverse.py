def reverseBits(n):
    # Write your code here.
    n = bin(n)[2:].zfill(32)
    rev = n[::-1]
    return int(rev,2)