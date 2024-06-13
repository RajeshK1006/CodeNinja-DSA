from typing import *

def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:
    # Write your code here.
    k = 0
    presumMap = {}
    presum = 0
    maxLen= 0

    for i in range(len(arr)):
        presum += arr[i]

        if presum ==k:
            maxLen = i+1

        remainder = presum - k
        if remainder in presumMap:
            l = i-presumMap[remainder]
            maxLen = max(l,maxLen)

        if presum not in presumMap:
            presumMap[presum] = i

    return maxLen