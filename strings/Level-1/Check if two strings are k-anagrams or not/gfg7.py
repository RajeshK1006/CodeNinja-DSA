#User function template for Python 3

class Solution:
    def areKAnagrams(self, s1, s2, k):
        # code here
        if len(s1)!=len(s2):
            return  0
        mapp = {}
        
        for char in s1:
            if char not in mapp:
                mapp[char] = 1
            else:
                mapp[char] +=1 
                
        for char in s2:
            if char in mapp:
                mapp[char] -=1
                
                if mapp[char]==0:
                    del mapp[char]
    
            
        c=0
        for i in mapp.values():
            if i!=0:
                c+=abs(i)
        
        if c<=k:
            return 1
        else:
            return 0
        
            
