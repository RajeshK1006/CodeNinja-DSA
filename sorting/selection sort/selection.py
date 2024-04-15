from typing import List

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):

            if i!=j and arr[j]<arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr