# Problem: 417. Pacific Atlantic Water Flow
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # visit neighboring cells north, south, east, and west
        directions = set(((-1, 0), (1, 0), (0, -1), (0, 1)))
        # keep track of cells that have access the Atlantic ocean
        atlantic = set()
        # keep track of cells that have access to the Pacific ocean
        pacific = set()

        # helper function for depth first search traversal
        def dfs(row, col, ocean, visited):
            # mark the current cell as visited
            visited.add((row, col))
            # mark that the current cell has acces to the ocean
            ocean.add((row, col))

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and heights[new_row][new_col] >= heights[row][col]
                    and ((new_row, new_col)) not in visited
                ):
                    # the neighboring cell's height is higher than or equal to the current cell's height
                    dfs(new_row, new_col, ocean, visited)

        # call dfs from border cells that have direct access to an ocean
        for i in range(rows):
            for j in range(cols):
                # border cells that have access to the Pacific ocean
                if i == 0 or j == 0:
                    visited = set()
                    pacific.add((i, j))
                    dfs(i, j, pacific, visited)
                # border cells that have access to the Atlantic ocean
                if i == rows - 1 or j == cols - 1:
                    visited = set()
                    atlantic.add((i, j))
                    dfs(i, j, atlantic, visited)

        # return the cells that have access to both oceans
        return [list(cell) for cell in pacific & atlantic]
