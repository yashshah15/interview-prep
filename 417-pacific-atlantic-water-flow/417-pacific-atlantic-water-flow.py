class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows =len(heights)
        cols = len(heights[0])
        
        pac = set()
        atl = set()
        
        def dfs(r, c, visited, previousHeight):
            if r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < previousHeight or (r,c) in visited:
                return
            
            visited.add((r, c))
            
            dfs(r + 1 ,c, visited, heights[r][c])
            dfs(r - 1 ,c, visited, heights[r][c])
            dfs(r ,c + 1, visited, heights[r][c])
            dfs(r ,c - 1, visited, heights[r][c])
            
            
        for j in range(cols):
            dfs(0, j, pac, heights[0][j])
            dfs(rows - 1, j, atl, heights[rows - 1][j])
            
        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols - 1, atl, heights[i][cols - 1])
            
        res =[]
            
        for i in range(rows):
            for j in range(cols):
                if (i, j) in atl and (i, j) in pac:
                    res.append([i, j])
            
        return res
            
            