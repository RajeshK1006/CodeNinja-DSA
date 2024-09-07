# cook your dish here
def check(n,x):
    
    slices = n*x
    pizz = slices//4
    p = slices%4
    if p:
        return pizz+1 
    else:
        return pizz
    
    
        
t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    print(check(n,x))
