# cook your dish here
def check(x,y):
    return (x-y) + (y//2)
    

x,y = map(int, input().split())
print(check(x,y))
