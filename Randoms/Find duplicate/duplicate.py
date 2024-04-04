def findDuplicate(arr):
    # Write your code here
    sett = set()
    for i in arr:
        if i not in sett:
            sett.add(i)
        else:
            return i
    
