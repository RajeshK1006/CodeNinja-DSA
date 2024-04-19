from os import *
from sys import *
from collections import *
from math import *

def bubbleSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            