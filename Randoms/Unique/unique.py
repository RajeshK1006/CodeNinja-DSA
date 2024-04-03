import sys

def findUnique(arr, n) :
    #Your code goes here
    for i in range(n):
        if arr.count(arr[i])==1:
            ans = arr[i]
    return ans 
