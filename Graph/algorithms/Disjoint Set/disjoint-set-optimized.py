# Disjoint Set (Union-Find data structure)
SIZE = 5


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    # function for the find operation: find the representative of a disjoint set
    # optimized implementation of the find operation - path compression
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # function for the find operation: find the representative of a disjoint set
    # optimized implementation of the union operation - union by rank
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        else:
            self.parent[parent_x] = parent_y
            self.rank[parent_x] += 1

    # function to check if two elements are in the same set
    def is_connected(self, x, y):
        if self.find(x) == self.find(y):
            return True

        return False

    # Output is:
    # True
    # False


def main():
    union_find = UnionFind(SIZE)
    union_find.union(0, 1)
    union_find.union(1, 2)
    union_find.union(3, 4)
    print("0 and 1 are in the same set: ", union_find.is_connected(0, 1))
    print("1 and 3 are in the same set: ", union_find.is_connected(1, 3))


if __name__ == "__main__":
    main()
