# cook your dish here
def check(n,x,y):
    if y%x==0:
        return "YES"
    return "NO"
    
t = int(input())
for i in range(t):
    n,x,y = map(int, input().split())
    print(check(n,x,y))
    
