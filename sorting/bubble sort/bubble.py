from typing import List

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    # sort the outer loop in reverse
    for i in range(n-1,0,-1):
        # the inner lopp in from zero to i-1
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp = arr[j+1]
                arr[j+1] =arr[j]
                arr[j] = temp
    return arr