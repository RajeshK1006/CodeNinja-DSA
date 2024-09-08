# cook your dish here
def check(x,y):
    if x==y:
        return "YES"
    if x/2<=y:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    print(check(x,y))
