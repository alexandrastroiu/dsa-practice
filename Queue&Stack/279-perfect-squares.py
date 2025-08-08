# Problem: 279. Perfect Squares
# Link: https://leetcode.com/problems/perfect-squares/


# implement a queue class with the basic methods
import math


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
    def numSquares(self, n: int) -> int:

        def bfs(root, target):
            visited = set()
            steps = 0
            queue = Queue()

            if root == target:
                return 0

            queue.enqueue(root)
            visited.add(root)

            while not queue.is_empty():
                size = queue.size()

                for node in range(size):
                    current_node = queue.peek()
                    if current_node == target:
                        return steps
                    for i in range(1, int(math.sqrt(current_node)) + 1):
                        value = current_node - i * i
                        if value >= 0 and value not in visited:
                            queue.enqueue(value)
                            visited.add(value)
                    queue.dequeue()
                steps += 1

        return bfs(n, 0)
