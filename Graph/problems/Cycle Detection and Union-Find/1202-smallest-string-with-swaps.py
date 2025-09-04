# Problem:  1202. Smallest String With Swaps
# Link: https://leetcode.com/problems/smallest-string-with-swaps/

# Approach:  Consider it a graph problem. Consider the pairs as connected nodes in the graph.
# We can sort each connected component alone to get the lexicographically minimum string.


# implement the union-find data structure
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    # function used to find the subset of an element (using path compression)
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # function used to do the union of two subsets (using union by rank)
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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        length = len(s)
        union_find = UnionFind(length)
        components = dict()

        # iterate through the pairs and merge the sets corresponding to the characters that can be swapped
        for pair in pairs:
            union_find.union(pair[0], pair[1])

        # map each character index to the set where it belongs using a hash map
        for i in range(length):
            root = union_find.find(i)
            if root in components:
                components[root].append(i)
            else:
                components[root] = [i]

        # convert the initial string to a list in order to modify it
        res = list(s)
        # iterate through the values in the dictionary
        for indices in components.values():
            chars = [s[i] for i in indices]
            # sort the indices that belong in the current connected component
            indices.sort()
            # sort the characters that belong in the current connected component
            chars.sort()
            # iterate through the sorted indices and sorted characters
            # replace the values in the array in the correct order
            for idx, char in zip(indices, chars):
                res[idx] = char

        # return the result string by using th ejoin method
        return "".join(res)
