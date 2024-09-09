# cook your dish here
def check(x):
    if x%4==0:
        return "GOOD"
    return "NOT GOOD"

t = int(input())
for i in range(t):
    x = int(input())
    print(check(x))
