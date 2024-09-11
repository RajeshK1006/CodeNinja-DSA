# cook your dish here
def check(x,y,t,u):
    m1 = abs(x-t)
    m2 = abs(y-u)
    return max(m1,m2)

t = int(input())
for i in range(t):
    x,y,m,n = map(int, input().split())
    print(check(x,y,m,n))
    
