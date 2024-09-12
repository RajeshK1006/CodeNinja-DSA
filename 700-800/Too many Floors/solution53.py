# cook your dish here
def check(x,y):
    if x%10==0:
        chef = x//10
    else:
        chef = x//10 +1
    if y%10==0:
        
        chefina = y//10 
    else:
        chefina = y//10 +1 
    
    if chef ==chefina:
        return 0 
    else:
        return abs(chef-chefina)
        
    
t = int(input())
for i in range(t):
    x,y = map(int,input().split())
    print(check(x,y))
