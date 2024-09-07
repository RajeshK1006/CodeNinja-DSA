# cook your dish here
def check(n):
    if n<=100:
        return n 
    elif 100<n<=1000:
        return n-25
    elif 1000<n<=5000:
        return n-100
    else:
        return n-500
    
t = int(input())
for _ in range(t):
    x = int(input())
    print(check(x))
