# cook your dish here
def check(total,x,y,z):
    rem = total - (x+y)
    if rem>=z:
        return 0
    else:
        if total - x >=z or total - y>=z:
            return 1 
        else:
            return 2
t = int(input())
for i in range(t):
    t,x,y,z = map(int, input().split())
    print(check(t,x,y,z))
