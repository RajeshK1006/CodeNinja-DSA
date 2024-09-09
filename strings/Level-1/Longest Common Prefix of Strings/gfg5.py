class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        arr.sort()
        c = 0
        for i in range(len(arr[0])):
            if arr[0][i] == arr[-1][i]:
                c+=1
            else:
                break
        if c:
            return arr[0][:c]
        else:
            return -1
