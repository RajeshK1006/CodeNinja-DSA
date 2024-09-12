# cook your dish here
def check(x,y,d):
    if abs(x-y)<=d:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    x,y,d = map(int,input().split())
    print(check(x,y,d))
    
