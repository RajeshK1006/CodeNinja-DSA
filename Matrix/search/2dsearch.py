def searchMatrix(mat, target: int) -> bool:
    # Write your code here.
    for i in range(len(mat)):
        if target>=mat[i][0] and target<=mat[i][len(mat[0])-1]:
            l = 0
            h = len(mat[0]) -1
            while l<=h:
                mid = (l+h)//2
                if target ==mat[i][mid]:
                    return True
                elif target<mid:
                    h = mid -1
                else:
                    l = mid +1
            return False
