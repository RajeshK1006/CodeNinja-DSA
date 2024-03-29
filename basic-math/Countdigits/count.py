def countDigits(n: int) -> int:
    number = str(n)
    c=0
    for i in number:
        if int(i)!=0:
            if n%int(i)==0:
                c+=1
    return c