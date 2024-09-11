# cook your dish here
def check(n,m):
    c = n/m
    if c%2==0:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    print(check(n,m))
