def check(n):
    if n+3>10:
        return "NO"
    else:
        return "YES"
    
t = int(input())
for i in range(t):
    n = int(input())
    print(check(n))
