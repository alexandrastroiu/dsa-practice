# Kruskal's Minimum Spanning Tree Algorithm

V = 5
# V - the number of vertices in the initial graph


# implement the union-find data structure
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.rank[parent_x] < self.rank[parent_y]:
                self.parent[parent_x] = parent_y
            elif self.rank[parent_x] > self.rank[parent_y]:
                self.parent[parent_y] = parent_x
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += 1


# helper function for Kruskal's Minimum Spanning Tree Algorithm
def kruskal(edges):
    # sort the edges in non-decreasing orded by weight
    edges = sorted(
        edges, key=lambda edge: edge[2]
    )  # initialize the union-find data structure
    union_find = UnionFind(V)
    cost = 0
    count = 0

    # traverse through all the edges in the sorted edge list
    for x, y, weight in edges:
        parent_x = union_find.find(x)
        parent_y = union_find.find(y)

        # if vertices x and y are not already connected add the edge that connects the vertices to the MST
        if parent_x != parent_y:
            print(f"({x}, {y}, {weight})")
            union_find.union(x, y)
            # add the weight of the current edge to the total cost of the MST
            cost += weight
            count += 1
            # the MST has V-1 edges
            if count == V - 1:
                break

    print(f"Minimum Weight: {cost}")

    # Output is:
    # Minimum Spanning Tree using Kruskal's algorithm:
    # (0, 1, 2)
    # (3, 4, 5)
    # (1, 3, 6)
    # (1, 2, 7)
    # Minimum Weight: 20


def main():
    edge_list = [[0, 1, 2], [0, 2, 8], [1, 2, 7], [1, 3, 6], [2, 3, 10], [3, 4, 5]]
    print("Minimum Spanning Tree using Kruskal's algorithm: ")
    kruskal(edge_list)


if __name__ == "__main__":
    main()
