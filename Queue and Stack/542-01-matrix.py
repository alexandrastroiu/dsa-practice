# Problem: 542. 01 Matrix
# Link: https://leetcode.com/problems/01-matrix/

# Solution based on multi-source BFS (efficient)
# shortest distance in a matrix/grid => BFS

# implement a queue class with the basic methods
class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.queue[0]

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        def bfs():
            directions = set(((0, 1), (0, -1), (1, 0), (-1, 0)))
            queue = Queue()

            for i in range(rows):
                for j in range(cols):
                    if mat[i][j] == 0:
                        queue.enqueue((i, j))
                    else:
                        mat[i][j] = float("inf")

            while not queue.is_empty():
                row, col = queue.dequeue()

                for x, y in directions:
                    new_row = row + x
                    new_col = col + y
                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and mat[new_row][new_col] > mat[row][col] + 1
                    ):
                        mat[new_row][new_col] = mat[row][col] + 1
                        queue.enqueue((new_row, new_col))

            return mat

        return bfs()


# Solution based on the classic bfs algortihm (leads to Time Limit Exceeded)

# implement a queue class with the basic methods
"""
class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.queue[0]

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return
        self.queue.pop(0)


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        directions = set(((0, -1), (0, 1), (1, 0), (-1, 0)))

        def bfs(row, col, target):
            root = mat[row][col]
            queue = Queue()
            visited = set()
            steps = 0

            queue.enqueue((row, col))
            visited.add((row, col))

            while not queue.is_empty():
                size = queue.size()
                for _ in range(size):
                    row, col = queue.peek()

                    if mat[row][col] == target:
                        return steps

                    for x, y in directions:
                        new_row = row + x
                        new_col = col + y

                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            if (new_row, new_col) not in visited:
                                visited.add((new_row, new_col))
                                queue.enqueue((new_row, new_col))

                    queue.dequeue()
                steps += 1

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] != 0:
                    mat[i][j] = bfs(i, j, 0)

        return mat
"""
