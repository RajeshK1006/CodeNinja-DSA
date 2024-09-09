# cook your dish here
def check(n ,arr):
    c = 0
    for i in range(n):
        if arr[i]>=1000:
            c+=1
    return c

t = int(input())
for i in range(t):
    n = int(input())
    arr =list(map(int, input().split()))
    print(check(n,arr))
