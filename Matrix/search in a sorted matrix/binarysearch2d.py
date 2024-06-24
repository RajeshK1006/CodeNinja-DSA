from typing import *

def binarysearch(arr,tar):
    l = 0
    h = len(arr)-1

    while l<=h:
        mid = (l+h)//2
        if arr[mid] == tar:
            return 1
        elif arr[mid]>tar:
            h = mid -1
        else:
            l = mid +1
    return 0

def searchElement(matrix : List[List[int]], target : int) -> int:
    # Write your code here
    row= len(matrix)
    col = len(matrix[0])-1

    for row in range(row):
        if  matrix[row][0] <= target and target<= matrix[row][len(matrix[0])-1]:
            return binarysearch(matrix[row],target)