class Solution:
    def romanToDecimal(self, s): 
        # code here
        mapp = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C':100,
                'D': 500,
                'M': 1000}
        res = mapp[s[-1]]
        for j in range(len(s)-2,-1,-1):
            if mapp[s[j]]>=mapp[s[j+1]]:
                res += mapp[s[j]]
            else:
                res -= mapp[s[j]]
        return res
