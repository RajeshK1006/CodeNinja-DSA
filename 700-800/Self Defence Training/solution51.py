# cook your dish here
def check(age,arr):
    c = 0
    for i in arr:
        if 10<=i<=60:
            c+=1 
    return c

t = int(input())
for i in range(t):
    age = int(input())
    arr = list(map(int, input().split()))
    print(check(age,arr))
