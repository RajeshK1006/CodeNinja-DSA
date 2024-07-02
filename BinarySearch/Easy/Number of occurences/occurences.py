from collections import Counter

def findfirst(a,m,target):
    l = 0
    h = m-1
    ans = -1
    while l<=h:
        mid  = (l+h)//2
        if a[mid] ==target:
            ans = mid
            h = mid -1
        elif a[mid]<target:
            l = mid +1
        else:
            h = mid - 1
    return ans

def findlast(a,m,target):
    l = 0
    h = m-1
    ans = -1
    while l<=h:
        mid  = (l+h)//2
        if a[mid] ==target:
            ans = mid
            l = mid +1
        elif a[mid]<target:
            l = mid +1
        else:
            h = mid - 1
    return ans
def count(arr, n: int, x: int) -> int:
    # Your code goes here
    first = findfirst(arr,n,x)
    last = findlast(arr,n,x)
    if first == -1:
        return 0
    else:
        return last - first +1