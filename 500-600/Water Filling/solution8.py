# cook your dish here
def check(x,y,z):
    if x+y+z<=1:
        return "Water filling time"
    return "Not now"

t = int(input())
for _  in range(t):
    x,y,z = map(int, input().split())
    print(check(x,y,z))
