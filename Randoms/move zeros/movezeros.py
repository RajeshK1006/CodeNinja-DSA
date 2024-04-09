def moveZeros(n,a):
    # Write your code here.
    for i in a:
        if i==0:
            a.remove(i)
            a.append(0)
    return a