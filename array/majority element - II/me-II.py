from math import *
from collections import *
from sys import *
from os import *

def majorityElementII(arr):
	# Write your code here.
	l =[]
	C= Counter(arr)

	for k,v in C.items():
		if C[k]>len(arr)//3:
			l.append(k)
	return l