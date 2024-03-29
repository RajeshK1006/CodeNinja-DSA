n=int(input())  
# taking n as a input 
## write your code !!
# def palindrome(n)
m = str(n)

if m == m[::-1]:
    print("true")
else:
    print("false")