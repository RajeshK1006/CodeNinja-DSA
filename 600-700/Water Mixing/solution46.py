# cook your dish here
def check(a,b,x,y):
    while a<b and x:
        a+=1 
        x-=1
    while a>b and y:
        a -= 1 
        y-= 1 
    if a==b:
        return "YES"
    else:
        return "No"
    
t = int(input())
for i in range(t):
    a,b,x,y = map(int, input().split())
    print(check(a,b,x,y))
