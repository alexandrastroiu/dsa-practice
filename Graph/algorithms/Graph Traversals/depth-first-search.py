# Depth First Search Traversal for an undirected, connected graph


# Recursive implementation of DFS
def dfs_recursive(adj_list, visited, vertex):
    # visit the current node and mark it as visited
    visited[vertex] = True
    print(vertex, end=" ")

    # for all its unvisited neighbors call dfs recursively
    for neighbor in adj_list[vertex]:
        if not visited[neighbor]:
            dfs_recursive(adj_list, visited, neighbor)


# Iterative implementation of DFS using a stack
def dfs_iterative(adj_list, visited, vertex):
    # initialize the stack
    stack = []
    # add the source vertex to the stack
    stack.append(vertex)

    # while the stack is not empty, continue the process
    while len(stack) > 0:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

            # add all the unvisited neighbors of the current node to the stack
            # the neighbors are pushed in reverse order because the stack removes the last added item first
            for neighbor in reversed(adj_list[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)


def main():
    # the adjacent list representation of the graph
    adj_list = [[1, 2, 3], [0, 4, 5], [0], [0, 5, 6], [1], [1, 3], [3]]
    # initialize a boolean array visited, the array is used to avoid visiting a node multiple times
    visited = [False for _ in range(len(adj_list))]

    # Output is:
    # Depth First Search Traversal - Recursive Implementation:
    # 0 1 4 5 3 6 2

    print("Depth First Search Traversal - Recursive Implementation: ")
    dfs_recursive(adj_list, visited, 0)
    print()

    # Output is:
    # Depth First Search Traversal - Iterative Implementation:
    # 0 1 4 5 3 6 2

    # initialize the visited array
    visited = [False for _ in range(len(adj_list))]
    print("Depth First Search Traversal - Iterative Implementation: ")
    dfs_iterative(adj_list, visited, 0)
    print()


if __name__ == "__main__":
    main()
