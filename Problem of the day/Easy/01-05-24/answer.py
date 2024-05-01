from os import *
from sys import *
from collections import *
from math import *

def shakeHands(friends, n, k):
	# Write your code here.
	i = 0
	while i <len(friends):
		if friends[i]==k:
			k=k*2
		i+=1
	return k