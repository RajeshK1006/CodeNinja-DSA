# cook your dish here
def check(p,t):
    
    return abs(p-t)

t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    print(check(x,y))
    
