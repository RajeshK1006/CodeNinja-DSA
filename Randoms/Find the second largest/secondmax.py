from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    arrr = sorted(list(set(sequenceOfNumbers)))
    if len(arrr)<=1:
        return -1
    else:
        return arrr[-2]