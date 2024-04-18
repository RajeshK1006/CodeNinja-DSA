def insertionSort(arr):
    # write your code here !!!
    for i in range(len(arr)):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            temp  = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            # arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1
    return arr