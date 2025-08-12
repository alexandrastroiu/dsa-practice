# Problem: 20. 133. Clone Graph
# Link: https://leetcode.com/problems/clone-graph/

# Refactored solution
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        visited = {}

        def clone(current_node):
            if current_node is None:
                return None

            if current_node in visited:
                return visited[current_node]

            visited[current_node] = Node(current_node.val)

            for neighbor in current_node.neighbors:
                visited[current_node].neighbors.append(clone(neighbor))

            return visited[current_node]

        return clone(node)


# Alternative solution
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # handle edge case: an empty graph
        if node is None:
            return None

        # handle edge case; the graph consists of only one node and it does not have any neighbors
        if not node.neighbors:
            new_node = Node(val=node.val)
            return new_node

        # helper function used to traverse the graph (DFS)
        def dfs(current, visited, map_nodes):
            # if the current node was not visited already
            if current.val not in visited:
                # mark the current node as visited
                visited.add(current.val)
                # deep copy of the current node
                copy_current = map_nodes[current.val]
                # go through all neighbors of the current node
                for neighbor in current.neighbors:
                    # if the neighbor was not visited before
                    if neighbor.val not in visited:
                        # create a depp copy of the neighbor
                        next_node = Node(val=neighbor.val)
                        # add it to the neighbor list of the deep copy node
                        copy_current.neighbors.append(next_node)
                        # map the index to the deep copy
                        # in order to avoid creating multiple deep copies of the same node
                        map_nodes[next_node.val] = next_node
                        # dfs
                        dfs(neighbor, visited, map_nodes)
                    else:
                        # add it to the neighbor list of the current node
                        # the deep copy of the neighbor was previously created
                        copy_current.neighbors.append(map_nodes[neighbor.val])

        # create a deep copy of the first node
        new_root = Node(val=1)
        # use a set to keep track of traversed nodes
        visited = set()
        # map the deep copy nodes and their index (the index is unique)
        map_nodes = {node.val: new_root}
        # call dfs function
        dfs(node, visited, map_nodes)

        # return the deep copy root
        return new_root
"""
