# cook your dish here

def check(arr):
    e = 0
    o = 0
    for i in range(len(arr)):
        if arr[i]%2==0:
            e+=1 
        else:
            o+=1 
    
    if e>o:
        return "READY FOR BATTLE"
    else:
        return "NOT READY"
        
        
t = int(input())

arr = list(map(int,input().split()))
print(check(arr))
