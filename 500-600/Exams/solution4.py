# cook your dish here
def check(x,y,z):
    if  (x*y)//2<z:
        return "YES"
    return  "NO"

t = int(input())
for i in range(t):
    x,y,z = map(int,input().split())
    print(check(x,y,z))

