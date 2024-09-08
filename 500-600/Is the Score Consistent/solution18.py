# cook your dish here
def check(a,b,c,d):
    if c>=a and d>=b:
        return "POSSIBLE"
    return "IMPOSSIBLE"

t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    print(check(a,b,c,d))
