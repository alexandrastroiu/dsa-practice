# Floyd-Warshall algorithm

# The algorithm works on graphs with negative edeg weights, but does not work on graphs with negative cycles

V = 5
INF = float("inf")


def floyd_warshall(edges):
    dist = [[INF for _ in range(V)] for _ in range(V)]

    for i in range(V):
        dist[i][i] = 0

    for edge in edges:
        u, v, weight = edge
        # for directed graphs
        dist[u][v] = weight

    # k - intermediate vertex
    # by the time vertex k is considered, all shortest paths using only vertices 0 to k-1 have already been computed
    for k in range(V):
        # i - source vertex
        for i in range(V):
            # destination vertex
            for j in range(V):
                # update the distance from i to j
                if dist[i][k] < INF and dist[k][j] < INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # return the shortest distance between all pairs of nodes in the graph
    return dist

    # Output is:
    # The shortest path distance between all the pairs of nodes in the graph using the Floyd-Warshall algorithm:
    #  6 9 10 11
    # inf 0 3 4 5
    # inf inf 0 1 2
    # inf inf inf 0 inf
    # inf inf inf -1 0


def main():
    edge_list = [[1, 3, 5], [4, 3, -1], [2, 4, 2], [1, 2, 3], [0, 1, 6]]
    distances = floyd_warshall(edge_list)

    print(
        "The shortest path distance between all the pairs of nodes in the graph using the Floyd-Warshall algorithm: "
    )
    for i in range(V):
        for j in range(V):
            print(distances[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()
