class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        opt =[[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+ 1)]
        max_square = 0
        
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) +1):
                if matrix[i - 1][j - 1] == "1":
                    opt[i][j] = min(opt[i][j - 1], opt[i - 1][j], opt[i - 1][j - 1]) + 1
                    max_square = max(max_square, opt[i][j])
        return max_square ** 2
        