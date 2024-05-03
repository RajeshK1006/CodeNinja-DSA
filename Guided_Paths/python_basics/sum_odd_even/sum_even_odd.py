#Your code goes here


num = input()
e = 0 
o = 0
for i in num:
    if int(i)%2==0:
        e+=int(i)
    else:
        o+=int(i)
print(e,end = " ")
print(o)
