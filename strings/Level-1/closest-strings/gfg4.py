class Solution:
	def shortestDistance(self, s, word1, word2):
		# code here
		mini = float("inf")
		last1 = -1
		last2 = -1
		for i in range(len(s)):
		    if s[i]==word1:
		        last1 = i
		    if s[i]==word2:
		        last2 = i
		    if last1!=-1 and last2!=-1:
		        
		        distance = abs(last2-last1)
		        
		        mini = min(mini,distance)
		return mini
