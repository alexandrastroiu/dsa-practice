# Problem: 743. Network Delay Time
# Link: https://leetcode.com/problems/network-delay-time/

import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # helper function for Dijkstra's algorithm
        def dijkstra(adj_list, source):
            # initialize the distance array
            dist = [float("inf")] * n
            # initialize the priority queue
            pq = []

            dist[source] = 0
            heapq.heappush(pq, (0, source))

            while pq:
                # remove the first node in the priority queue (the node with the minimum distance)
                node = heapq.heappop(pq)[1]

                # iterate through the current node's adjacent nodes
                for pair in adj_list[node]:
                    adj, weight = pair[0], pair[1]

                    # if there is a shorter path to the adjacent node through the current node
                    # update the distance and add the ndoe to the priority queue
                    if dist[adj] > dist[node] + weight:
                        dist[adj] = dist[node] + weight
                        heapq.heappush(pq, (dist[adj], adj))

            return dist

        adj_list = [[] for _ in range(n)]

        for time in times:
            u, v, w = time[0], time[1], time[2]
            # nodes in the network are labeled from 1 to n
            u -= 1
            v -= 1
            # create the adjacency list from the given edge list
            adj_list[u].append((v, w))

        distances = dijkstra(adj_list, k - 1)

        # return the minimum time it takes for all the n nodes to receive the signal
        # if it is impossible for all the n nodes to receive the signal, return -1
        return max(distances) if float("inf") not in distances else -1
