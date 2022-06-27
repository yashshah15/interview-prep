class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = []
        c = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    c = c + 1
                    queue.append((i, j))
                    grid[i][j] = "0"
                    while len(queue) > 0:
                        (row, col) = queue.pop(0)
                        if row + 1 < m and grid[row + 1][col] == "1":
                            queue.append((row + 1,col))
                            grid[row + 1][col] = "0"
                        
                        if row - 1 >= 0 and grid[row - 1][col] == "1":
                            queue.append((row - 1,col))
                            grid[row - 1][col] = "0"
                        
                        if col + 1 < n and grid[row][col + 1] == "1":
                            queue.append((row,col + 1))
                            grid[row][col + 1] = "0"
                        
                        if col - 1 >= 0 and grid[row][col - 1] == "1":
                            queue.append((row,col - 1))
                            grid[row][col - 1] = "0"
        
        return c 