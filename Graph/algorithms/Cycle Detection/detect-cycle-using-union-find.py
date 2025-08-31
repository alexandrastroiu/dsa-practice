# Detect cycle in an undirected graph using union-find algorithm
V = 4


# function used to find the subset of an element
def find_parent(parent, x):
    if parent[x] == x:
        return x

    return find_parent(parent, parent[x])


# function used to do the union of two subsets
def union(parent, x, y):
    parent[x] = y


def main():
    adj_list = [[1, 2], [0, 2], [0, 1, 3], [2]]
    # initialize the parent array
    parent = [0] * V
    is_cyclic = False

    # initialize all subsets
    # initially each subset contains a single node which is its own parent
    for node in range(V):
        parent[node] = node

    # iterate through all edges using the adjacency list
    # place two adjacent node in the same subset (do the union of their subsets)
    # if two adjhacent nodes are already in the same subset => there is a cycle in the graph
    for node in range(V):
        for adjacent_node in adj_list[node]:
            parent_node = find_parent(parent, node)
            parent_adj = find_parent(parent, adjacent_node)

            if parent_node == parent_adj:
                is_cyclic = True

            union(parent, parent_node, parent_adj)

    # Output is:
    # The graph contains a cycle.

    if is_cyclic:
        print("The graph contains a cycle.")
    else:
        print("The graph does not contain a cycle.")


if __name__ == "__main__":
    main()
