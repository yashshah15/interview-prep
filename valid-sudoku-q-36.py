class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        horizontal = [None] * 9
        vertical = [None] * 9
        grid = [None] * 9
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".": continue
                    
                if horizontal[i] == None: horizontal[i] = set()
                elif board[i][j] in horizontal[i]: return False
                
                if vertical[j] == None: vertical[j] = set()
                elif board[i][j] in vertical[j]: return False
                
                gridIndex = (i // 3) * 3 + (j // 3)
                if grid[gridIndex] == None: grid[gridIndex] = set()
                elif board[i][j] in grid[gridIndex]: return False
                
                horizontal[i].add(board[i][j])
                vertical[j].add(board[i][j])
                grid[gridIndex].add(board[i][j])
                print grid
            
        return True
