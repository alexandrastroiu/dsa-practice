# Topological Sorting based on Breadth First Search (Khan's Algorithm)
# Topological Sorting for a directed acyclic graph (DAG)
V = 6


def topological_sort(adj_list, queue, indegree):
    while len(queue) > 0:
        # remove the current node and print it
        node = queue.pop(0)
        print(node, end=" ")

        # iterate through the adjacent nodes of the current node
        for adj_node in adj_list[node]:
            # decrease the in-degree of the adjacent nodes
            indegree[adj_node] -= 1
            # add to the queue only the adjacent nodes that have the in-degree 0
            if indegree[adj_node] == 0:
                queue.append(adj_node)


def main():
    # the adjacent list representation of the graph
    adj_list = [[1, 2], [5], [], [4], [], [4]]
    # initialize the in-degree for the nodes in the graph
    indegree = [0] * V

    # iterate through the adjacency list and calculate the in-degree for each node
    for i in range(V):
        for j in adj_list[i]:
            indegree[j] += 1

    # initialize the queue with the nodes that have the in-degree 0
    queue = [node for node in range(V) if indegree[node] == 0]

    # Output is:
    # Topological Sorting:
    # 0 3 1 2 5 4

    # topological sorting order may not be unique

    print("Topological Sorting: ")

    topological_sort(adj_list, queue, indegree)


if __name__ == "__main__":
    main()
