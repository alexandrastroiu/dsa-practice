# Problem: 752. Open the Lock
# Link: https://leetcode.com/problems/open-the-lock/


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
        if self.is_empty():
            return
        self.queue.pop(0)


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # helper function for getting the directions (the combinations done in only one move)
        def directions(string: str):
            dirs = (
                (-1, 0, 0, 0),
                (0, -1, 0, 0),
                (0, 0, -1, 0),
                (0, 0, 0, -1),
                (1, 0, 0, 0),
                (0, 1, 0, 0),
                (0, 0, 1, 0),
                (0, 0, 0, 1),
            )
            # dirs contains the possible moves (1 step back/forward in 4 possible positions)
            result = []

            for d0, d1, d2, d3 in dirs:
                chars = [0] * 4
                # wrap around if the value is past 9
                chars[0] = str((int(string[0]) + d0) % 10)
                chars[1] = str((int(string[1]) + d1) % 10)
                chars[2] = str((int(string[2]) + d2) % 10)
                chars[3] = str((int(string[3]) + d3) % 10)
                result.append("".join(chars))

            # return resulting combinations
            return result

        # helper function for BFS in order to obtain the shortest path length to the target combination
        def bfs(root, target):
            queue = Queue()
            visited = set()
            # use a visited set because there are cycles
            dead_set = set(deadends)
            # convert the list to a set for faster look up

            # if the root ("0000") is a dead end, the target cannot be reached
            if root in dead_set:
                return -1

            # start BFS
            steps = 0
            queue.enqueue(root)
            visited.add(root)

            while not queue.is_empty():
                size = queue.size()
                for _ in range(size):
                    current_node = queue.peek()
                    # if the target combination is found, return the minimum number of turns
                    if current_node == target:
                        return steps
                    for node in directions(current_node):
                        # avoid visited nodes and nodes that represent dead ends
                        if node not in visited and node not in dead_set:
                            queue.enqueue(node)
                            visited.add(node)

                    queue.dequeue()
                steps += 1
                # update the steps

            return -1
            # it never reaches the target combination

        return bfs("0000", target)
        # call bfs with root as "0000"
