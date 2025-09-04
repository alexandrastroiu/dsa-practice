# Topological Sorting based on Depth First Search
# Topological Sorting for a directed acyclic graph (DAG)
V = 6


# function for topological sorting based on DFS
def topological_sort(adj_list, node, visited, stack):
    # mark the current node as visited
    visited[node] = True

    # iterate through the adjacent nodes of the current node
    for adj_node in adj_list[node]:
        # for unvisited adjacent nodes call the function
        if not visited[adj_node]:
            topological_sort(adj_list, adj_node, visited, stack)

    # use another stack to get the topological order of the nodes in the graph
    stack.append(node)


def main():
    # the adjacent list representation of the graph
    adj_list = [[1, 2], [5], [], [4], [], [4]]
    # initialize a boolean array visited, the array is used to avoid visiting a node multiple times
    visited = [False] * V
    # initialize the stack
    stack = []

    # iterate through the nodes and call the helper function for each unvisited node
    for i in range(V):
        if not visited[i]:
            topological_sort(adj_list, i, visited, stack)

    # Output is:
    # Topological Sorting:
    # 3 0 2 1 5 4

    # topological sorting order may not be unique

    print("Topological Sorting: ")

    while len(stack) > 0:
        print(stack.pop(), end=" ")


if __name__ == "__main__":
    main()
