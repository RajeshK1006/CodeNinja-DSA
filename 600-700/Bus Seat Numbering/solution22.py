# cook your dish here
def check(n):
    if 1<=n<=10:
        return "LOWER DOUBLE"
    elif 11<=n<=15:
        return "LOWER SINGLE"
    elif 16<=n<=25:
        return "UPPER DOUBLE"
    else:
        return  "UPPER SINGLE"
    
t = int(input())
for i in range(t):
    n = int(input())
    print(check(n))
