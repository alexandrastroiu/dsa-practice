# Bellman-Ford Algorithm

# The Bellman-Ford algorithm works on graphs with negative edge weights, but does not work on graphs that contain negative weight cycles

V = 5
INF = float("inf")


# helper function for Bellman-Ford algorithm
def bellman_ford(edges, source):
    # initialize the distance from the given source node to all the other nodes in the graph with infinite value
    dist = [INF] * V
    # the distance from the source node to itself is 0
    dist[source] = 0

    for i in range(V):
        # track if any relaxation was made in the current interation using a boolean variable
        change = False
        # iterate through the edges
        for edge in edges:
            u, v, weight = edge

            # relaxation of edges
            if dist[u] != INF and dist[v] > dist[u] + weight:

                # detect negative cycles
                if i == V - 1:
                    return -1

                dist[v] = dist[u] + weight
                change = True

        # optimization => exit the loop early if there is no distance updated in an iteration
        if not change:
            break

    # return the shortest distance from the source node to all other nodes in the graph
    return dist


def main():
    edge_list = [[1, 3, 5], [4, 3, -1], [2, 4, 2], [1, 2, 3], [0, 1, 6]]
    # call the helper function
    distances = bellman_ford(edge_list, 0)

    # Output is:
    # Shortest distances from the source node to all other nodes in the graph using the Bellman-Ford algorithm:
    # [0, 6, 9, 10, 11]

    print(
        "Shortest distances from the source node to all other nodes in the graph using the Bellman-Ford algorithm: "
    )
    print(distances)


if __name__ == "__main__":
    main()
