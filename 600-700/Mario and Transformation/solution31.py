# cook your dish here
def check(x):
    x = x%3
    if x==0:
        return "NORMAL"
    elif x==1:
        return 'HUGE'
    else:
        return "SMALL"
t = int(input())
for i in range(t):
    n = int(input())
    print(check(n))
