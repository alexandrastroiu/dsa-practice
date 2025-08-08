# Problem: 200. Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/

# Time Complexity: O(m * n)  (all cells in the grid are traversed once)
# Space Complexity: O(m * n) (due to recursion stack)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # a nested function used for dfs traversal
        def dfs(row, col):
            grid[row][col] = "0"
            # the cell is marked as visited
            for x, y in directions:
                new_row = row + x
                # the row of the neighbouring cell
                new_col = col + y
                # the column of the neighbouring cell
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == "1"
                ):
                    # check if the cell is lan ('1') and the row and column of the cell are in bounds
                    dfs(new_row, new_col)
                    # recursive call if the neighbouring cell is land

        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        # count separate isalands in the grid
        directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
        # check for land cells in 4 directions: west, north, east, south

        # goes through all the cells in the grid
        for i in range(rows):
            for j in range(cols):
                # if a cell is land
                if grid[i][j] == "1":
                    islands += 1
                    # a new island is found
                    dfs(i, j)
                    # call dfs to traverse all cells in the island and mark them

        return islands
        # return the number of separate islands
