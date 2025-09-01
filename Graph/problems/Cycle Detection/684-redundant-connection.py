# Problem:  684. Redundant Connection
# Link: https://leetcode.com/problems/redundant-connection/

# using the Union-Find algorithm (more efficient)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # function used to find the subset of an element
        def find_parent(parent, x):
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])

            return parent[x]

        # function used to do the union of two subsets
        def union(parent, x, y):
            parent[x] = y

        # initialize the parent array
        parent = [i for i in range(len(edges))]

        # iterate through all the edges
        for edge in edges:
            u = edge[0] - 1
            v = edge[1] - 1
            parent_u = find_parent(parent, u)
            parent_v = find_parent(parent, v)

            # the vertices are in the same subset => there is a cycle
            if parent_u == parent_v:
                return edge

            # merge the sets
            union(parent, parent_u, parent_v)

        return []

    # approach using DFS (less efficient)
    """
    class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # create the adjacency list from the edge list 
        def add_edges():
            adj_list = [[] for _ in range(len(edges))]

            for edge in edges:
                u = edge[0]
                v = edge[1]
                adj_list[u - 1].append(v - 1)
                adj_list[v - 1].append(u - 1)

            return adj_list
        
        # function for cycle detection using depth first search traversal
        def dfs_util(adj_list, node, visited, parent, cycles):
            visited.add(node)

            for adj in adj_list[node]:
                if adj in visited and adj != parent:
                    cycles.append([min(node + 1, adj + 1), max(node + 1, adj + 1)])
                elif adj not in visited:
                    dfs_util(adj_list, adj, visited, node, cycles)  
            
            
        
        adj_list = add_edges()
        cycles = []
        ans = []
        
        # call dfs for each node and add all edges that could create a cycle
        for node in range(len(edges)):
            visited = set()
            dfs_util(adj_list, node , visited, -1, cycles)
       
        # find the edge that creates the cycle that is the last in the input
        for edge in edges:
            if edge in cycles:
                ans = edge
        
        return ans
    """
