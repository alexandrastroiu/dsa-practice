# Represent a graph through the adjacency matrix (unweighted and undirected graph)

# V represents the number of vertices in the graph
V = 5


# Function used to add an edge between two vertices
def add_edge(matrix, source, dest):
    # mark in the matrix that an edge exists between the source node and the destination node
    matrix[source][dest] = 1
    # the graph is undirected (mark from source to destination and from destination to source)
    matrix[dest][source] = 1


# Function used to display the adjacency matrix of the graph
def display_matrix(matrix):
    print("Adjacency Matrix Representation")

    for i in range(V):
        for j in range(V):
            print(matrix[i][j], end=" ")
        print()


def main():
    # initialize the adjacency matrix with zeros (the matrix has V rows and V columns)
    adj_matrix = [[0] * V for _ in range(V)]

    # add edges
    add_edge(adj_matrix, 0, 1)
    add_edge(adj_matrix, 1, 2)
    add_edge(adj_matrix, 1, 3)
    add_edge(adj_matrix, 1, 4)
    add_edge(adj_matrix, 3, 4)

    # display the adjacency matrix
    display_matrix(adj_matrix)


if __name__ == "__main__":
    main()
