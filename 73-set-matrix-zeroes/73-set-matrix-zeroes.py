class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        is_first_col = False
        
        for i in range(rows):
            if matrix[i][0] == 0:
                is_first_col = True
            
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if not matrix[i][0]  or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0
        
        if is_first_col:
            for i in range(rows):
                matrix[i][0] = 0