class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,s1,s2):
        if len(s1)!=len(s2):
            return False
            
        mapp = {}
        visited = set()
        
        for k,v in zip(s1,s2):
            if k in mapp:
                if mapp[k]!=v:
                    return False 
            else:
                if v in visited:
                    return False
                else:
                    mapp[k] = v 
                    visited.add(v)
        return True
