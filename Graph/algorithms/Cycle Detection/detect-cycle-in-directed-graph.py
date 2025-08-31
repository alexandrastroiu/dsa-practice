# Detect cycle in a directed graph using DFS
V = 5


# helper function to check if a cycle exists in the graph using DFS
def dfs_util(adj_list, node, visited, stack):
    # mark the current node as visited
    visited[node] = True
    # mark the current node as present in the recursion call stack
    stack[node] = True

    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            if dfs_util(adj_list, neighbor, visited, stack):
                return True
        # there is an edge leading to an ancestor => there is a cycle
        elif stack[neighbor]:
            return True

    # remove the node from the recursion stack (backtrack)
    stack[node] = False
    return False


def main():
    adj_list = [[1], [2], [3], [2], [0]]
    # initialize a boolean array visited, the array is used to avoid visiting a node multiple times
    visited = [False] * V
    # initialize a boolean array used to keep track of nodes that are in the current recursion call stack
    stack = [False] * V
    is_cyclic = False

    for i in range(V):
        if not visited[i]:
            if dfs_util(adj_list, i, visited, stack):
                is_cyclic = True
                break

    # Output is:
    # The graph contains a cycle.

    if is_cyclic:
        print("The graph contains a cycle.")
    else:
        print("The graph does not contain a cycle.")


if __name__ == "__main__":
    main()
