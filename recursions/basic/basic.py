from typing import List


def recurs(count,x,result):
    if count>x:
        return result
    result.append(count)
    count+=1
    return recurs(count,x,result)
def printNos(x: int) -> List[int]: 
    # Write your code here
    return recurs(1,x,[])
    