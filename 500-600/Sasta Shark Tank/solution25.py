# cook your dish here
def check(x,y):
    val1 = x*10
    val2 = y*5
    if val1>val2:
        return "FIRST"
    elif val2>val1:
        return "SECOND"
    else:
        return "ANY"
    
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    print(check(x,y))
