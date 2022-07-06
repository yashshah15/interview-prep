class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        c = 0 
        res = []
        left, up = 0, 0
        right, down = cols - 1, rows - 1
        
        while c < rows * cols:
            #traverse left to right
            for i in range(left, right + 1):
                res.append(matrix[up][i])
                c += 1 
            
            #traverse top to bottom 
            for i in range(up + 1, down + 1):
                res.append(matrix[i][right])
                c += 1
            
            if up != down:
                 #traverse from right to left
                for i in range(right - 1, left -1, -1):
                    res.append(matrix[down][i])
                    c += 1
            
            if left != right:
                #traverse bottom to top
                for i in range(down - 1, up, -1):
                    res.append(matrix[i][left])
                    c += 1
            
            #update pointers
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return res