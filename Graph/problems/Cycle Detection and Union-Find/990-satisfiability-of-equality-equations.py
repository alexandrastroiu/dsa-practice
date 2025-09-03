# Problem:  990. Satisfiability of Equality Equations
# Link: https://leetcode.com/problems/satisfiability-of-equality-equations/


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
    def equationsPossible(self, equations: List[str]) -> bool:
        # use a dictionary to map the variables to their index
        variables = dict()
        count = 0

        # iterate through the equations
        # add all the distinct variables in the dictionary
        for eq in equations:
            if eq[0] not in variables:
                variables[eq[0]] = count
                count += 1
            if eq[3] not in variables:
                variables[eq[3]] = count
                count += 1

        # initialize the union-find data structure
        union_find = UnionFind(len(variables))

        # iterate through the equations
        # find the equality equations and merge the sets of the corresponding variables
        for eq in equations:
            if eq[1] == "=" and eq[2] == "=":
                union_find.union(variables[eq[0]], variables[eq[3]])

        # iterate through the equations
        # if two variables must be different but they are in the same set => the equations cannot be satisfied at the same time
        for eq in equations:
            if eq[1] == "!":
                parent_x = union_find.find(variables[eq[0]])
                parent_y = union_find.find(variables[eq[3]])
                if parent_x == parent_y:
                    return False

        # the given equations can be satisfied at the same time
        return True
