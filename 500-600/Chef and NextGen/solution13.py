# cook your dish here
def check(a,b,x,y):
    if a*b<=x*y:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    a,b,x,y = map(int,input().split())
    print(check(a,b,x,y))
