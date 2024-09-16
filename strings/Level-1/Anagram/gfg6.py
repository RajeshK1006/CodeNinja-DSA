class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,s1,s2):
        #code here
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
            else:
                return "NO"
        
        for i in mapp.values():
            if i!=0:
                return "NO"
        
        return "YES"
