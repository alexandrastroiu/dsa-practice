# Prim's Algorithm for Minimum Spanning Tree

V = 5
# V - the number of vertices in the initial graph

import heapq


# helper function for converting the edge list into the adjacency list
def create_adjlist(edges):
    adj_list = [[] for _ in range(V)]

    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))

    return adj_list


# helper function for Prim's algorithm
def prims(adj, source):
    # initialize the priority queue
    pq = []
    # use a boolean array in order to avoid processing visited vertices multiple times
    visited = [False] * V
    # calculate the cost of the MST
    cost = 0

    # Pick a random vertex
    # At first, the mST consists of a single vertex
    heapq.heappush(pq, (0, source))

    while pq:
        # the top element from the priority queue is the one with the smallest weight
        weight, u = heapq.heappop(pq)

        # avoid already visited vertices
        if visited[u]:
            continue

        # mark the current vertex as visited (u is now part of the MST)
        visited[u] = True
        # add the weight of the current edge to the cost of the MST
        cost += weight

        # traverse the adjacent vertices of the current vertex
        for v, w in adj[u]:
            # push unvisited adjacent vertices to the priority queue
            if not visited[v]:
                heapq.heappush(pq, (w, v))

    return cost

    # Output is:
    # Cost of the Minimum Spanning Tree using Prim's algorithm: 20


def main():
    edge_list = [[0, 1, 2], [0, 2, 8], [1, 2, 7], [1, 3, 6], [2, 3, 10], [3, 4, 5]]
    adj_list = create_adjlist(edge_list)
    print(
        f"Cost of the Minimum Spanning Tree using Prim's algorithm: {prims(adj_list, 0)}"
    )


if __name__ == "__main__":
    main()
