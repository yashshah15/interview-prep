class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        row=None
        for i in range(rows):
            if target >= matrix[i][0] and target <= matrix[i][cols-1]:
                row=i
        
        if row==None:
            return False
        
        beg=0
        end=cols-1
        mid= (beg+end)//2
        while beg <= end:
            if matrix[row][mid] == target:
                return True
            
            if target < matrix[row][mid]:
                end=mid-1
            
            elif target > matrix[row][mid]:
                beg=mid+1
            
            mid= (beg+end)//2
        
        return False