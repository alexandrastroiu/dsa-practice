# 1584. Min Cost to Connect All Points

import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        adj_list = [[] for _ in range(length)]
        vertices = dict()

        for index, point in enumerate(points):
            vertices[index] = point

        for i in range(length):
            for j in range(i + 1, length):
                manhattan_dist = abs(vertices[i][0] - vertices[j][0]) + abs(
                    vertices[i][1] - vertices[j][1]
                )
                adj_list[i].append((j, manhattan_dist))
                adj_list[j].append((i, manhattan_dist))

        def prims(adj, source):
            pq = []
            visited = [False] * length
            heapq.heappush(pq, (0, source))
            cost = 0

            while pq:
                w, u = heapq.heappop(pq)

                if visited[u]:
                    continue

                visited[u] = True
                cost += w

                for v, weight in adj[u]:
                    if not visited[v]:
                        heapq.heappush(pq, (weight, v))

            return cost

        return prims(adj_list, 0)
