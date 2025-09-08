# Dijkstra's Algorithm (using Min Heap)

# The algorithm works for a connected graph with no negative edge weights

import heapq

V = 6


# helper function for Dijkstra's algorithm
def dijkstra(adj_list, source):
    # initialize the distance from the given source node to all the other nodes in the graph
    dist = [float("inf")] * V
    # initialize the priority queue
    pq = []

    # the distance from the source ndoe to itself is 0
    dist[source] = 0
    # add the source node to the priority queue
    heapq.heappush(pq, (0, source))

    while pq:
        # remove the first node in the priority queue (the node with the minimum distance)
        current_node = heapq.heappop(pq)[1]

        # iterate through the current node's adjacent nodes
        for pair in adj_list[current_node]:
            adj_node, weight = pair[0], pair[1]

            # if there is a shorter path to the adjacent node through the current node
            # update the distance and add the ndoe to the priority queue
            if dist[adj_node] > dist[current_node] + weight:
                dist[adj_node] = dist[current_node] + weight
                heapq.heappush(pq, (dist[adj_node], adj_node))

    # return the array with the shortest distance from the given source to all other nodes
    return dist


def main():
    adj_list = [
        [(1, 4), (2, 8)],
        [(4, 6), (0, 4)],
        [(3, 2), (0, 8)],
        [(4, 10), (2, 2)],
        [(3, 10), (1, 6), (5, 8)],
        [(4, 8)],
    ]
    # call the helper function for Dijkstra's algorithm with 0 as the given source node
    distance = dijkstra(adj_list, 0)

    # Output is:
    # The sortest distance from the given source node to all other nodes in the graph using Dijkstra's algorithm:
    # The shortest distance from the source to the vertex 1 is: 4
    # The shortest distance from the source to the vertex 2 is: 8
    # The shortest distance from the source to the vertex 3 is: 10
    # The shortest distance from the source to the vertex 4 is: 10
    # The shortest distance from the source to the vertex 5 is: 18

    print(
        "The shortest distance from the given source node to all other nodes in the graph using Dijkstra's algorithm: "
    )

    for node in range(1, V):
        print(
            f"The shortest distance from the source to the vertex {node} is: {distance[node]}"
        )


if __name__ == "__main__":
    main()
