# cook your dish here
def check(x,y,z):
    rem = y//x
    if rem<z:
        return z-rem
    else:
        return min(0,rem)
    
t = int(input())
for i in range(t):
    x,y,z = map(int, input().split())
    print(check(x,y,z))
