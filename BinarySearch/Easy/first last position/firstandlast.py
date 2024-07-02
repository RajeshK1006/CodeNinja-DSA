from os import *
from sys import *
from collections import *
from math import *

def findfirst(a,target):
    l = 0
    h = len(a) -1
    ans = -1
    while l<=h:
        mid = (l+h)//2
        if a[mid]==target:
            ans = mid
            h = mid -1
        elif a[mid]<target:
            l = mid +1
        else:
            h = mid - 1
    return ans

def findlast(a,target):
    l = 0
    h = len(a) -1
    ans = -1
    while l<=h:
        mid = (l+h)//2
        if a[mid]==target:
            ans = mid
            l = mid + 1
        elif a[mid]<target:
            l = mid +1
        else:
            h = mid -1
    return ans


def firstAndLastPosition(arr, n, k):
    first = findfirst(arr,k)
    last = findlast(arr,k)
    return first , last