# Convert Adjacency List to Adjacency Matrix of a graph


def convert_list(adj_list):
    vertices = len(adj_list)
    # initialize the adjacency matrix with zeros (the matrix has V rows and V columns)
    matrix = [[0] * vertices for _ in range(vertices)]

    for source in range(vertices):
        for dest in adj_list[source]:
            matrix[source][dest] = 1

    return matrix


# Function used to display the adjacency matrix of the graph
def display_matrix(matrix):
    print("Adjacency Matrix Representation")

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()


def main():
    adj_list = [[1, 2], [0, 2, 3], [0, 1], [1]]

    adj_matrix = convert_list(adj_list)
    display_matrix(adj_matrix)


if __name__ == "__main__":
    main()
