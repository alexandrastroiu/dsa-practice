# Problem: 841. Keys and Rooms
# Link: https://leetcode.com/problems/keys-and-rooms/

# the rooms matrix can be represented as a graph
# each room is a node and each key is an edge
# we need to check if all rooms can be visited (the graph is connected)
# the graph can be traversed using DFS or BFS in order to check this


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
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        # visited is a set, it can contain only unique values
        # if len(visited) == number of rooms, then it is guaranteed that all rooms were visited

        # helper function for BFS traversal
        def bfs(root):
            # initialize the queue
            queue = Queue()
            # start from room 0
            queue.enqueue(root)
            visited.add(0)

            # traverse all rooms (if it is possible)
            while not queue.is_empty():
                current_room = queue.dequeue()

                # visit all rooms that are opened with the keys from the current room
                # if they are unvisited
                for key in current_room:
                    if key and key not in visited:
                        visited.add(key)
                        queue.enqueue(rooms[key])

        # call the bfs function
        bfs(rooms[0])

        return len(visited) == len(rooms)
