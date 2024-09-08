# cook your dish here
def check(arr):
    arr.sort(reverse = True)
    summ = sum(arr[1:])
    if arr[0]>summ:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    arr = list(map(int,input().split()))
    print(check(arr))
