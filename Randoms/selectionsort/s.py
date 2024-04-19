from os import *
from sys import *
from collections import *
from math import *

def selectionSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                arr[j],arr[mini]= arr[mini],arr[j]
                