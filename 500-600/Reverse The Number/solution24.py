# cook your dish here
def check(n):
    return int(n[::-1])

t = int(input())
for i in range(t):
    n = input()
    print(check(n))
