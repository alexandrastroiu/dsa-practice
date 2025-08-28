# Problem: 1091. Shortest Path in Binary Matrix
# Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # adjacent cells of the path are 8-directionally connected
        directions = set(
            ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        )
        # initialize the queue
        queue = []
        # use a set to keep track of already visited cells
        visited = set()

        # edge case: the first cell is not 0 or the last cell is not 0
        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1

        # edge case: the grid contains only once cell with the value 0
        if rows == 1:
            return 1

        # helper function for breadth first search tarversal
        def bfs(row, col):
            queue.append((row, col))
            visited.add((row, col))
            length = 1

            while len(queue) > 0:
                size = len(queue)
                for _ in range(size):
                    row, col = queue.pop(0)
                    # check if the bottom-right corner was reached
                    if row == rows - 1 and col == cols - 1:
                        return length
                    for dx, dy in directions:
                        new_row = row + dx
                        new_col = col + dy
                        if (
                            0 <= new_row < rows
                            and 0 <= new_col < cols
                            and grid[new_row][new_col] == 0
                        ):
                            if (new_row, new_col) not in visited:
                                visited.add((new_row, new_col))
                                queue.append((new_row, new_col))
                length += 1

            return -1

        # call bfs function from the top-left cell
        return bfs(0, 0)
