# cook your dish here

def check(x,y):
    return x*4+y
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    print(check(x,y))
