from sys import *
from collections import *
from math import *

def getLongestSubarray(nums, k: int) -> int:
    # Write your code here
    pressumMap = {}
    presum = 0

    maxLen = 0

    for i in range(len(nums)):
        presum += nums[i]
        
        if presum == k:
            maxLen = max(maxLen,i+1)

        rem = presum - k
        
        if rem in pressumMap:
            l = i - pressumMap[rem]
            maxLen = max(maxLen ,l)
        
        if presum not in pressumMap:
            pressumMap[presum] = i
    return maxLen