# write your solution here

def read_matrix():
    with open("matrix.txt") as matrix_file:
        matrix = []
        for line in matrix_file:
            line = line.replace("\n","")
            parts = line.split(",")
            int_parts = list(map(int, parts))
            matrix.append(int_parts)
    return matrix


def matrix_sum():
    matrix = read_matrix()
    mat_sum = 0
    for line in matrix:
        line_sum = sum(line)
        mat_sum += line_sum
    return mat_sum

def matrix_max():
    matrix = read_matrix()
    mat_max = 0
    for line in matrix:
        for element in line:
            if element > mat_max:
                mat_max = element
    return mat_max

def row_sums():
    matrix = read_matrix()
    sum_list = []
    for line in matrix:
        sum_list.append(sum(line))
    return sum_list

if __name__ == "__main__":
    matrix = read_matrix()
    mat_sum = matrix_sum()
    mat_max = matrix_max()
    sum_list= row_sums()
    print(matrix, mat_sum, mat_max, sum_list)