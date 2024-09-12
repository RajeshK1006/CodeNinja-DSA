# cook your dish here
def check(r,A,B):
    summ  = 0
    for i in range(1,r+1):
        if i%2==0:
            summ += A
        else:
            summ += B
    return summ


t = int(input())
for i in range(t):
    e,x,y = map(int, input().split())
    print(check(e,x,y))
