# cook your dish here
def check(a,b,c,d):
    x1 = a+c
    x2 = a+d 
    x3 = b+c 
    x4 = b+d
    return max(x1,x2,x3,x4)

t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    print(check(a,b,c,d))
