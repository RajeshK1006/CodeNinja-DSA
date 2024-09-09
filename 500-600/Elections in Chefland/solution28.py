# cook your dish here
def check(n,x,arr):
    c = 0
    for i in range(n):
        if arr[i]>=x:
            c+=1 
    return c

t = int(input())
for i in range(t):
    n , x = map(int, input().split())
    arr = list(map(int, input().split()))
    print(check(n,x,arr))
