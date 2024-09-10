# cook your dish here
def check(n,x):
    if n>x:
        return "NO"
    if x%n==0:
        return "YES"
    else:
        return "NO"
    
t = int(input())
for i in range(t):
    n,x = map(int, input().split())
    print(check(n,x))
