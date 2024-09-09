#User function template for Python 3

class Solution:
    def convertRoman(self, n):
        mapp = [
        ('M', 1000),
        ('CM', 900),
        ('D', 500),
        ('CD', 400),
        ('C', 100),
        ('XC', 90),
        ('L', 50),
        ('XL', 40),
        ('X', 10),
        ('IX', 9),
        ('V', 5),
        ('IV', 4),
        ('I', 1)
        ]
        res = ""
        for k,v in mapp:
            while n>=v:
                res+=k
                n = n-v
        return res#Code here
