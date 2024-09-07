# cook your dish here
def cash(n,x):
    if n==0:
        return 0
    if n<6:
        return x
    rem= n%6
    q = n//6
    if rem==0:
        return q*x
    else:
        return q*x+x

t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    ans = cash(n,x)
    print(ans)
