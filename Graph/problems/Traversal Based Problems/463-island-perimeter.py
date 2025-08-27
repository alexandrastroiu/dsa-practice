# Problem: 463. Island Perimeter
# Link: https://leetcode.com/problems/island-perimeter/


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # land cells connect 4-directionally
        directions = set(((0, -1), (0, 1), (-1, 0), (1, 0)))
        # keep track of visited cells using a set
        visited = set()

        # helper function for depth first serach traversal
        def dfs(row, col) -> int:
            # mark the current cell as visited
            visited.add((row, col))
            perimeter = 0

            # search for land cells in 4 directions from the current land cell
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                # call dfs from the adjacent land cell and update the perimeter
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if grid[new_row][new_col] and (new_row, new_col) not in visited:
                        perimeter += dfs(new_row, new_col)
                    elif grid[new_row][new_col] == 0:
                        perimeter += 1
                else:
                    perimeter += 1

            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)
