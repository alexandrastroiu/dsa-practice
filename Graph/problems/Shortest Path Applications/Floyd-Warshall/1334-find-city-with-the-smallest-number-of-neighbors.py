# Problem: 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
# Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

# Approach: Floyd-Warshall algorithm
# Alternative solution: run Dijkstra's algorithm for each vertex in the graph

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def floyd_warshall():
            dist = [[float('inf') for _ in range(n)] for _ in range(n)]

            for i in range(n):
                dist[i][i] = 0
            
            for edge in edges:
                u, v, weight = edge
                dist[u][v] = weight
                dist[v][u] = weight
            
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
            
            return dist
        
        distances = floyd_warshall()
        minimum_reachable = float('inf')
        cities = {}
        
        for i in range(n - 1, -1, -1):
            count = 0
            for j in range(n):
                if i != j and distances[i][j] <= distanceThreshold:
                    count += 1
            cities[i] = count
            minimum_reachable = min(minimum_reachable, count)
        
        for city in cities:
            if cities[city] == minimum_reachable:
                return city
        