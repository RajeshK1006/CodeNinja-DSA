# cook your dish here
def check(arr,x):
    if x in arr:
        return "YES"
    return "NO"


arr = list(map(int, input().split()))
x = arr.pop()
print(check(arr,x))
    
