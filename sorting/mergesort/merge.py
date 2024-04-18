def mergeSort(arr, l: int, r: int):
    # Write Your Code Here
    if l>=r:
        return 
    mid = (l+r)//2
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)

def merge(arr,l,mid,r):
    t = []
    left = l
    right = mid+1
    while left<=mid and right<=r:
        if arr[left]<=arr[right]:
            t.append(arr[left])
            left+=1
        else:
            t.append(arr[right])
            right+=1
    while left<=mid:
        t.append(arr[left])
        left+=1
    while right<=r:
        t.append(arr[right])
        right+=1
    for i in range(l,r+1):
        arr[i] = t[i-l]
