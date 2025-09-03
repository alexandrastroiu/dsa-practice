# Problem: 1319. Number of Operations to Make Network Connected
# Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/


# use the union-find data structure
# alternative solution: find the number of connected components by using graph traversal algorithms (dfs/bfs)


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    # the find operation (using path compression)
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # the union operation (using union by rank)
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_x] = parent_y
            self.rank[parent_y] += 1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # initially there are n separate sets
        union_find = UnionFind(n)
        disconnected = 0
        extra_cables = 0

        # iterate through all the connections
        # merge the sets of the connected computers
        for connection in connections:
            parent_x = union_find.find(connection[0])
            parent_y = union_find.find(connection[1])

            # if there is a cycle (two computers are connected in more than one way) => there is an extra connection
            # count extra cables (extra edges that lead to cycles)
            if parent_x == parent_y:
                extra_cables += 1
            else:
                union_find.union(connection[0], connection[1])

        # count the number of connected components
        for computer in range(n):
            if union_find.parent[computer] == computer:
                disconnected += 1

        # the minimum number of cables that have to be moved is the number of connected components - 1
        return disconnected - 1 if extra_cables >= disconnected - 1 else -1
