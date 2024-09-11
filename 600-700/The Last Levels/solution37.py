# cook your dish here
def check(x,y,z):
    rest = x//3
    if x%3==0:
        rest = rest -1
    return (x*y)+(rest *z) 

t = int(input())
for i in range(t):
    x,y,z = map(int, input().split())
    print(check(x,y,z))
    
