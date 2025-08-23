# Represent a graph through the adjacency list (unweighted and undirected graph)

# V represents the number of vertices in the graph
V = 5


# Function used to add an edge between two vertices
def add_edge(list, source, dest):
    # mark in the matrix that an edge exists between the source node and the destination node
    list[source].append(dest)
    # the graph is undirected (mark from source to destination and from destination to source)
    list[dest].append(source)


# Function used to display the adjacency list of the graph
def display_list(list):
    print("Adjacency List Representation")

    for source in range(V):
        print(f"{source}:", end="")
        for dest in list[source]:
            print(dest, end=" ")
        print()


def main():
    # initialize the adjacency list (each index in the list represents a vertex in the graph)
    # the list at an index n contains the vertices that are adjacent to the vertex n
    adj_list = [[] for _ in range(V)]

    # add edges
    add_edge(adj_list, 0, 1)
    add_edge(adj_list, 0, 2)
    add_edge(adj_list, 2, 3)
    add_edge(adj_list, 2, 4)
    add_edge(adj_list, 3, 4)

    # display the adjacency list
    display_list(adj_list)


if __name__ == "__main__":
    main()
