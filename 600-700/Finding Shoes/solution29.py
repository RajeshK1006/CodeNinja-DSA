# cook your dish here
def check(n,x):
    if n<x:
        return n
    pairs = n*2 - x
    return pairs


t = int(input())
for i in range(t):
    n,x = map(int, input().split())
    print(check(n,x))
