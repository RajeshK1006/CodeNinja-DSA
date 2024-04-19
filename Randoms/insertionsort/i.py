from os import *
from sys import *
from collections import *
from math import *

from typing import List

def insertionSort(n: int, arr: List[int]) -> None:
    # Write your code here.
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
            