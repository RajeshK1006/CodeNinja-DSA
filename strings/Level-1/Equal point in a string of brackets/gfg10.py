class Solution:
    def findIndex(self,s):
        open_count = 0
        for i in range(len(s)):
            if s[i] == "(":
                open_count+=1 
        
        close_count = 0
        point = -1 
        
        for i in range(len(s)-1,-1,-1):
            if s[i] ==")":
                close_count+=1
            else:
                open_count -=1 
            
            
            if close_count == open_count:
                point = i 
        
        return len(s) if point==-1 else point
