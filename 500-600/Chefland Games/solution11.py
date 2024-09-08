# cook your dish here
def check(a,b,c,d):
    if a+b+c+d==0:
        return "IN"
    else:
        return "OUT"
    
t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    print(check(a,b,c,d))
