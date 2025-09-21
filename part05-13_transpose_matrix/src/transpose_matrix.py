def transpose(matrix: list):
    size = len(matrix)
    temp = []
    for i in range(size):
        for j in range(i+1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    matrix = [[2, 3, 4, 5], [6, 7, 8, 9], [9, 8, 7, 6], [5, 4, 3, 2]]

    print(matrix)

    matrix = transpose(matrix)

    print(matrix)