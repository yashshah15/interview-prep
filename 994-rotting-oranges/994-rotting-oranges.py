from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        #count number of fresh oranges
        fresh_oranges = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                #store the cell number of rotten oranges
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))
        
        #Run BFS to rot the oranges
        minutes = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, column = queue.popleft()
            if row == -1:
                minutes += 1
                if queue:
                    queue.append((-1, -1))
            
            else:
                #We encountered a rotten orange
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], column + d[1]
                    if rows> neighbor_row >= 0 and cols > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))
        
        return minutes if fresh_oranges == 0 else -1
        