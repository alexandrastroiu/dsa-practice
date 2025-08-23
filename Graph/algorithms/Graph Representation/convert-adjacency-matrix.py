# Convert Adjacency Matrix to Adjacency List of a graph


def convert_matrix(matrix):
    vertices = len(matrix)
    # initialize the adjacency list (each index in the list represents a vertex in the graph)
    # the list at an index n contains the vertices that are adjacent to the vertex n
    adj_list = [[] for _ in range(vertices)]

    for i in range(vertices):
        for j in range(vertices):
            if matrix[i][j] == 1:
                adj_list[i].append(j)

    return adj_list


# Function used to display the adjacency list of the graph
def display_list(adj_list):
    print("Adjacency List Representation")

    for source in range(len(adj_list)):
        print(f"{source}:", end="")
        for dest in adj_list[source]:
            print(dest, end=" ")
        print()


def main():
    adj_matrix = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0]]

    adj_list = convert_matrix(adj_matrix)
    display_list(adj_list)


if __name__ == "__main__":
    main()
