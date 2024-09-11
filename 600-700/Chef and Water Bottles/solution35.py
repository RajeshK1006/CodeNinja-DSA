# cook your dish here
def check(n,x,y):
    if y<x:
        return min(n,0)
    else:
        return min(n,y//x)

t = int(input())
for i in range(t):
    n,x,y  = map(int, input().split())
    print(check(n,x,y))
