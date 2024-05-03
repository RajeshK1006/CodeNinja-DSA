#Your code goes here

n = int(input())
if n<0:
    print("Error")
elif n==0:
    print(1)
else:
    i = 1
    fact = 1
    while i<=n:
        fact *=i
        i+=1
    print(fact)
