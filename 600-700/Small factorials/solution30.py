# cook your dish here
def factorial(n):
    if n==0:
        return 1
    ans = 1 
    for i in range(1,n+1):
        ans*=i 
    return ans

t = int(input())
for i in range(t):
    n = int(input())
    print(factorial(n))
