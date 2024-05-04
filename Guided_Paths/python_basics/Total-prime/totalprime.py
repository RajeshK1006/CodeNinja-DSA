from os import *
from sys import *
from collections import *
from math import *

def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
    return True
    # return False


#Write your totalPrime function here.
def totalPrime(S,E):
    c=0
    for i in range(S,E+1):
        if prime(i):
            c+=1
    return c
