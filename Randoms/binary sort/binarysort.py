def sortBinaryArray(arr, n):
    # Write your code here
    cunt_0 = arr.count(0)
    return [0]*cunt_0 + [1]*(n-cunt_0)