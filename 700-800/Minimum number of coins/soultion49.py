# cook your dish here
def check(m):
    if m%10!=0 and m%5!=0:
        return -1
    if m%10==0:
        return m//10
    
    return m//10 +1 

t = int(input())
for i in range(t):
    m = int(input())
    print(check(m))
        
