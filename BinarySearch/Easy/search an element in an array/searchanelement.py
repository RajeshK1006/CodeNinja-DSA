from os import *
from sys import *
from collections import *
from math import *
def binays(a,target):
    l = 0
    h = len(a)-1
    while l<=h:
        mid = (l+h)//2
        if a[mid] == target:
            return 1
        elif a[mid]>target:
            h = mid -1
        else:
            l = mid +1
    return 0

def searchInSortedArray(arr,n,queries,q):
    # Write your code here.
    lst = []
    arr.sort()
    for i in range(len(queries)):
        ans = lst.append(binays(arr,queries[i]))
    return lst