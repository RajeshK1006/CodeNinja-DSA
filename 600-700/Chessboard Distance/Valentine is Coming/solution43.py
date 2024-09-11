# cook your dish here
def check(x,y):
    if x<y:
        return 0
    else:
        return  x//y 
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    print(check(x,y))
