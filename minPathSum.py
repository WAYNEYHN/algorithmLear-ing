#
# 
# @param matrix int整型二维数组 the matrix
# @return int整型
#
class Solution:
    def minPathSum(self , matrix ):
        # write code here
        
        if matrix is None or  len(matrix) < 1 or len(matrix[0]) < 1:
            return 0
        length = len(matrix)
        length_1=  len(matrix[0])
        dp = [[0 for i in range(length_1)] for j in range(length)]
        for i in range(length):
            for j in range(length_1):
                if i==0 and j ==0:
                    dp[0][0] = matrix[0][0]
                elif i==0:
                    dp[i][j] = dp[i][j-1] + matrix[i][j]
                elif j==0:
                    dp[i][j] = dp[i-1][j] + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + matrix[i][j]
        return dp[-1][-1]


class Solution:
    def minPathSum(self , matrix ):
        # write code here
        
        if matrix is None or  len(matrix) < 1 or len(matrix[0]) < 1:
            return 0
        length = len(matrix)
        length_1=  len(matrix[0])
        for i in range(length):
            for j in range(length_1):
                if i != 0 and j != 0:
                     matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j]) + matrix[i][j]
                elif i==0 and j ==0:
                    matrix[0][0] = matrix[0][0]
                elif i==0:
                    matrix[i][j] = matrix[i][j-1] + matrix[i][j]
                elif j==0:
                    matrix[i][j] = matrix[i-1][j] + matrix[i][j]
        return matrix[-1][-1]