# cook your dish here
def check(s):
    mapp = {"A":"T","T":"A","C":"G","G":"c"}
    rev  = ""
    for i in range(len(s)):
        rev += mapp[s[i]]
    return rev  

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    print(check(s))
        
