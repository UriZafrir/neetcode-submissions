from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set()
        
        def dfs(r: int, c: int) -> int:
            # 1. Base Case: Stop if out of bounds
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0
                
            # 2. Base Case: Stop if it is water or already explored
            if grid[r][c] == 0 or (r, c) in visited:
                return 0
                
            # 3. Mark this specific coordinate as visited
            visited.add((r, c))
            
            # 4. Count this current tile of land
            island_size = 1
            
            # 5. Add the land found by exploring all four directions
            island_size += dfs(r + 1, c)  # Down
            island_size += dfs(r - 1, c)  # Up
            island_size += dfs(r, c + 1)  # Right
            island_size += dfs(r, c - 1)  # Left
            
            return island_size
        
        max_area = 0
        
        # 6. Check every single tile in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # Only trigger a DFS search if we hit unvisited land
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_island_area = dfs(r, c)
                    
                    # Track our highest score manually instead of using max()
                    if current_island_area > max_area:
                        max_area = current_island_area
                        
        return max_area
