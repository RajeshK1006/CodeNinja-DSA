def findfloor(arr,m,y):
    l = 0
    h = m-1
    ans = -1
    while l<=h:
        mid = (l+h)//2
        if arr[mid]<=y:
            ans = arr[mid]
            l = mid +1
        else:
            h = mid -1
    return ans

def findceil(arr,m,y):
    l = 0
    h = m-1
    ans = -1
    while l<=h:
        mid = (l+h)//2
        if arr[mid]>=y:
            ans = arr[mid]
            h = mid -1
        else:
            l = mid +1
    return ans



def getFloorAndCeil(a, n, x):
    # Write your code here.
    floor = findfloor(a,n,x)
    ceil = findceil(a,n,x)
    return floor , ceil