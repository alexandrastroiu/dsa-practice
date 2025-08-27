# Problem: 994. Rotting Oranges
# Link: https://leetcode.com/problems/rotting-oranges/


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        # search for adjacent fresh oranges in 4 directions
        directions = set(((-1, 0), (1, 0), (0, 1), (0, -1)))
        # initialize the queue
        queue = []
        fresh = 0

        # helper function for breadth first search
        def bfs(num):
            minutes = 0
            # the number of fresh oranges in the grid
            fresh = num

            while len(queue) > 0:
                level_size = len(queue)
                # process elements level by level
                for _ in range(level_size):
                    row, col = queue.pop(0)
                    # search for adjacent fresh oranges in 4 directions
                    for dx, dy in directions:
                        new_row = row + dx
                        new_col = col + dy
                        if (
                            0 <= new_row < rows
                            and 0 <= new_col < cols
                            and grid[new_row][new_col] == 1
                        ):
                            # turn the fresh orange into a rotten orange
                            grid[new_row][new_col] = 2
                            # update the number of fresh oranges in the grid
                            fresh -= 1
                            # continue adding rotten oranges to the queue
                            queue.append((new_row, new_col))
                if queue:
                    # update the time elapsed
                    minutes += 1

            return minutes if fresh == 0 else -1

        # add all rotten oranges to the queue (start bfs traversal from multiple sources simultaneously)
        # count the number of fresh oranges in the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # handle edge case: there are no fresh oranges at minute 0
        if not fresh:
            return 0

        # call bfs in order to calculate the minimum time elapsed until there are no fresh oranges
        return bfs(fresh)
