# cook your dish here
def check(n):
    total =  n * 50
    cp = (70/100)*total
    profit = total - cp
    return int(profit)

t = int(input())
for i in range(t):
    n = int(input())
    print(check(n))
