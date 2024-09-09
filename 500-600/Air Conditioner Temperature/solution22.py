# cook your dish here
def check(a,b,c):
    if a<=b and c<=b:
        return "YES"
    return "NO"


t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    print(check(a,b,c))
