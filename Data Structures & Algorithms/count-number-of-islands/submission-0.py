class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set() # set to check if item was visited
        islands = 0
        
        def dfs(r, c):
            # 1. Out of bounds check MUST come first
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # 2. Check if water or already visited
            if grid[r][c] == "0" or (r, c) in visited:
                return
                
            # 4. Action: Add (r, c) to visited before checking neighbors
            visited.add((r, c))
            
            # 5. Recurse: Call dfs on top, bottom, left, right
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(rows):
            for c in range(cols):
                # 2. Main Scan: Only trigger DFS if it's land AND NOT in visited
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands