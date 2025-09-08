# Problem:  802. Find Eventual Safe States
# Link: https://leetcode.com/problems/find-eventual-safe-states/

# Approach: use a variation of the topological sorting algorithm
# Alternative solution: DFS


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = []
        length = len(graph)
        outdegree = [0] * length
        prev = [[] for _ in range(length)]

        # iterate through the node in the graph and calculate the out-degree using the given edges list
        for node in range(length):
            outdegree[node] = len(graph[node])

        # iterate through the nodes in the graph and their adjacent nodes
        # uses the given edge list to build the adjacency list of the reverse directed graph
        for node in range(length):
            for adj_node in graph[node]:
                prev[adj_node].append(node)

        # initialize the queue with the terminal nodes (a node is a terminal node if there are no outgoing edges)
        # terminal nodes are safe nodes
        queue = [node for node in range(length) if outdegree[node] == 0]

        # starting from the terminal nodes find nodes that can only be reached from terminal nodes
        # a node is a safe node if every possible path starting from that node leads to a terminal node => a safe node can only be reached from terminal nodes

        while len(queue) > 0:
            node = queue.pop(0)
            safe_nodes.append(node)

            for previous in prev[node]:
                outdegree[previous] -= 1
                # only safe nodes are added to the queue and to the result list
                if outdegree[previous] == 0:
                    queue.append(previous)

        safe_nodes.sort()

        # return the list of safe nodes in ascending order
        return safe_nodes
