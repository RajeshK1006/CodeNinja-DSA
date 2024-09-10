# cook your dish here
def check(arr):
    return max(arr)

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    print(check(arr))
