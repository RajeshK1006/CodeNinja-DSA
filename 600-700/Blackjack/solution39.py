# cook your dish here
def check(arr):
    summ = sum(arr)
    res = 21-summ
    if 1<=res<=10:
        return res
    else:
        return -1

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    print(check(arr))
