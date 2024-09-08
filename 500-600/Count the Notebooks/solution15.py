# cook your dish here
def check(n):
    pages = n*1000
    notes = pages//100
    return notes

t = int(input())
for i in range(t):
    n = int(input())
    print(check(n))
