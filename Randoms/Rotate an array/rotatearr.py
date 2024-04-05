def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    if k>len(arr):
        k= k%len(arr)
    for i in range(k):
        m = arr.pop(0)
        arr.append(m)
    return arr