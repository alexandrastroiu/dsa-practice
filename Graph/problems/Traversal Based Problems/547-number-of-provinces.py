# Problem: 547. Number of Provinces
# Link: https://leetcode.com/problems/number-of-provinces/


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])
        # keep track of visited cities using a set
        visited = set()
        provinces = 0

        # helper function for depth first search traversal
        def dfs(row):
            # mark the current city as visited
            visited.add(row)

            # call dfs for unvisited adjacent cities
            for index, element in enumerate(isConnected[row]):
                if element == 1 and index not in visited:
                    dfs(index)

        # the input grid is similar to an adjacency matrix
        # parse all the cities
        for i in range(rows):
            if i not in visited:
                # call dfs for each unvisited city
                dfs(i)
                # update the number of provinces
                # equivalent to counting the number of connected components
                provinces += 1

        # return the number of provinces
        return provinces
