# cook your dish here
def check(n,x):
    if n==x:
        return 0
    return min(n-x,x)

t = int(input())
for i in range(t):
    n,x = map(int, input().split())
    print(check(n,x))
