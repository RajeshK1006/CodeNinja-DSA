class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        res = S.split(".")
        return  ".".join(res[::-1])
