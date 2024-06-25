def search(arr, n, k):

    # Write your code here
    l = 0
    h = len(arr) - 1
    while l<=h:
        mid = (l+h)//2
        if arr[mid] == k:
            return mid
        elif arr[l]<=arr[mid]:
            if arr[l]<=k<=arr[mid]:
                h = mid -1
            else:
                l = mid +1
        else:
            if arr[mid]<=k<=arr[h]:
                l = mid +1
            else:
                h = mid -1
    return -1