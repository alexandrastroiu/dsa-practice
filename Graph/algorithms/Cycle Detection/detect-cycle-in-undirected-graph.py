# Detect cycle in an undirected graph using DFS
V = 4


# helper function to check if a cycle exists in the graph using DFS
def dfs_util(adj_list, node, visited, parent):
    # mark the current node as visited
    visited[node] = True

    for neighbor in adj_list[node]:
        # there is an adjacent node that was already visited and it is not the current node's parent => there is a cycle
        if visited[neighbor] and neighbor != parent:
            return True
        # for unvisited adjacent nodes call the function
        elif not visited[neighbor]:
            if dfs_util(adj_list, neighbor, visited, node):
                return True

    return False


def main():
    adj_list = [[1, 2], [0, 2], [0, 1, 3], [2]]
    # initialize a boolean array visited, the array is used to avoid visiting a node multiple times
    visited = [False] * V
    is_cyclic = False

    for i in range(V):
        if not visited[i]:
            if dfs_util(adj_list, i, visited, -1):
                is_cyclic = True
    # Output is:
    # The graph contains a cycle.

    if is_cyclic:
        print("The graph contains a cycle.")
    else:
        print("The graph does not contain a cycle.")


if __name__ == "__main__":
    main()
