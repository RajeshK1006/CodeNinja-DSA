def check(x,y):
    if x==y:
        return "SAME"
    elif x<y:
        return "BIKE"
    else:
        return "CAR"
    
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    print(check(x,y))
