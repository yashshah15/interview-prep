class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        opt = [[1] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                opt[i][j] = opt[i - 1][j] + opt[i][j - 1]
        
        return opt[-1][-1]
    