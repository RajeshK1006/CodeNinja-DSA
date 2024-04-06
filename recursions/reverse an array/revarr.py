from typing import *

def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    return rev(nums,n)

def rev(arr,length,result = []):
    if length==0 or not arr:
        return result

    m = arr.pop(-1)
    result.append(m)
    # length-=1
    return rev(arr,length-1,result)
