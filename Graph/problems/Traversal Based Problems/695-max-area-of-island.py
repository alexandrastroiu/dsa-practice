# Problem: 695. Max Area of Island
# Link: https://leetcode.com/problems/max-area-of-island/


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # land cells connect 4-directionally
        directions = set(((0, -1), (0, 1), (-1, 0), (1, 0)))
        max_area = 0
        # keep track of visited cells using a visited set
        visited = set()

        # helper function for depth first serach
        def dfs(row, col):
            # mark the current cell as visited
            visited.add((row, col))
            # the current area is 1
            area = 1

            # search for land cells in 4 directions from the current land cell
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # an adjacent unvisited land cell is found
                    if grid[new_row][new_col] and (new_row, new_col) not in visited:
                        # call dfs from the adjacent land cell and update the area
                        area += dfs(new_row, new_col)

            # return the area of the current island
            return area

        for i in range(rows):
            for j in range(cols):
                # call dfs for each unvisited land cell and update the maximum area of an island
                # equivalent to traversing all connected components of a graph
                if grid[i][j] and (i, j) not in visited:
                    max_area = max(max_area, dfs(i, j))

        return max_area
