# cook your dish here
def check(x,a,b):
    if a+(b*2)>=x:
        return "Qualify"
    return "NotQualify"

t = int(input())
for i in range(t):
    x,a,b = map(int,input().split())
    print(check(x,a,b))
