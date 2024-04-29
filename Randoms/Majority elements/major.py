from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(arr, n):
	# s = set(arr)
	c = Counter(arr)
	# Write your code here.
	for i, k in c.items():
		if  k>n//2:
			return i 
		
	return -1