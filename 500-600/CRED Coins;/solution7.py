# cook your dish here
def cehck(x,y):
    ans = (x*y)//100
    return ans

t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    print(cehck(x,y))
