# Problem: 130. Surrounded Regions
# Link: https://leetcode.com/problems/surrounded-regions/


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        # a cell is connected to adjacent cells horizontally or vertically
        directions = set(((-1, 0), (1, 0), (0, 1), (0, -1)))

        # helper function for depth first search traversal
        def dfs(row, col):
            # mark the current cell as safe
            # the current cell is a 'O' cell or directly or indirectly connected to a 'O' edge cell
            board[row][col] = "."

            # search for adjacent '0' cells connected to the current safe cell
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and board[new_row][new_col] == "O"
                ):
                    # call dfs the adjacent 'O' cell
                    dfs(new_row, new_col)

        # call dfs for 'O' edge cells
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (
                    i == 0 or i == rows - 1 or j == 0 or j == cols - 1
                ):
                    dfs(i, j)

        # mark 'O' cells left as surrounded
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # turn safe cells marked with '.' back to 'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ".":
                    board[i][j] = "O"
