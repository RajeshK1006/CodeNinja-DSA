class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        check = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(check)):
            if check[i] not in s.lower():
                return False 
        return True
