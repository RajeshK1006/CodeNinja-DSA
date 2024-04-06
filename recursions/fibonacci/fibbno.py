from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    # Write your code here
    arr = [0,1]
    return fibb(n,arr)
    
def fibb(limit,result):
    if limit ==1:
        return [0]
    if len(result)==limit:
        return result
    ele = result[-1]+result[-2]
    result.append(ele)
    return fibb(limit,result)