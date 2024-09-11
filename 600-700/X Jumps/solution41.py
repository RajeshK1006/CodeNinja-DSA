# cook your dish here
def check(x,y):
    if y==1:
        return x
    if x%y==0:
        return x//y
    else:
        c = 0
        while x>y:
            x-=y
            c+=1
        return c+x
    
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    print(check(x,y))
            
