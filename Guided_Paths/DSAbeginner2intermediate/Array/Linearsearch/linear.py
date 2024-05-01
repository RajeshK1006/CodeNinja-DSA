def linearSearch(n: int, num: int, arr) -> int:
    # Write your code here.
    if num not in arr:
        return -1
    else:
        for i in range(n):
            if arr[i] == num:
                return i