# cook your dish here
def check(p,q):
    summ = p+q
    if (summ//2)%2==0:
        return "Alice"
    else:
        return "Bob"
    
t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    print(check(x,y))
