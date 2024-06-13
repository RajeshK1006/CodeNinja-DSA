from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    maxi = 0
    sums= 0
    # for  i in range(n):
    #     for j in range(i,n):
    #         s = 0
            
    #         for k in range(i,j+1):
    #             s+=arr[k]
            
    #         maxi = max(s,maxi)

    # return maxi
    # for i in range(n):
    #     s = 0
    #     for j in range(i,n):
    #         s+=arr[j]

    #         maxi = max(maxi,s)
    # return maxi
    for i in range(n):
        sums+=arr[i]

        if sums<0:
            sums = 0

        maxi = max(maxi,sums)

    return maxi
