def search(matrix, x):
    # Write your code here.
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] ==x:
                return [i,j]
    return [-1,-1]