def searchInsert(arr, m: int) -> int:
    # Write your code here.
    ans = len(arr)

    l = 0
    h = len(arr) -1
    while l<=h:
        mid = (l+h)//2
        if arr[mid]>=m:
            ans= mid
            h = mid -  1
        else:
            l  = mid + 1
    return ans