# cook your dish here
def check(x,y):
    person = y*2
    total = x//person
    return total

t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    print(check(x,y))
