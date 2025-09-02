# Disjoint Set (Union-Find data structure)
SIZE = 5


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    # function for the find operation: find the representative of a disjoint set
    # naive implementation of the find operation
    # worst time complexity is linear
    def find(self, x):
        if self.parent[x] == x:
            return x

        return self.find(self.parent[x])

    # function for the union operation: merges two disjoint sets into a single set
    # naive implementation of the union operation
    # worst time complexity is linear
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        self.parent[parent_x] = parent_y

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
