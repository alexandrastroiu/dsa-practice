# Breadth First Search Traversal for an undirected, connected graph


# implement a class for queue
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return -1


# Implementation of BFS
def bfs(adj_list, visited, vertex):
    # initialize the queue
    queue = Queue()
    # add the source vertex to the queue
    queue.enqueue(vertex)
    # mark the source node as visited
    visited[vertex] = True

    # while the queue is not empty, continue the process
    while not queue.is_empty():
        # remove the vertex that is at the front of the queue and visit it
        node = queue.dequeue()
        print(node, end=" ")

        # add all unvisited adjacent vertices of the current node to the queue and mark them as visited
        # vertices are traversed level by level
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.enqueue(neighbor)


def main():
    # the adjacent list representation of the graph
    adj_list = [[1, 2, 3], [0, 4, 5], [0], [0, 5, 6], [1], [1, 3], [3]]
    # initialize a boolean array visited, the array is used to avoid visiting a node multiple times
    visited = [False for _ in range(len(adj_list))]

    # Output is:
    # Breadth First Search Traversal:
    # 0 1 2 3 4 5 6

    print("Breadth First Search Traversal: ")
    bfs(adj_list, visited, 0)
    print()


if __name__ == "__main__":
    main()
