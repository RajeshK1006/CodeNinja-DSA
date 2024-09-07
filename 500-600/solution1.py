# cook your dish here
def average(a,b,c):
    avg = (a+b)/2
    if avg>c:
        return "YES"
    else:
        return "NO"
        
        
t = int(input())
for i in range(t):

    a,b,c = map(int,input().split())
    
    ans = average(a,b,c)
    print(ans)
