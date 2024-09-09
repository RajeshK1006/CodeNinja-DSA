# cook your dish here
def seats(n):
    distance1 = 100-n
    distance2 = n-1
    if distance2<=distance1:
        return "LEFT"
    else:
        return "RIGHT"
    
t = int(input())
for i in range(t):
    n = int(input())
    print(seats(n))
