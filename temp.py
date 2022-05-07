matrix = [
    [1, 1, 0, 2],
    [1, 1, 1, 2],
    [2, 2, 0, 2],
    [0, 0, 0, 1]
]

def f(matrix, k):
    step = 0
    for n in range(k):
        while(matrix_general_count(matrix, n) > 0):
            matrix_bubble(matrix, matrix_info_per_element(matrix, n), n)
            step = step + 1

    return step

def matrix_info_per_element(matrix, element_searched):
    max_count_x, max_count_y = 0, 0
    index_x, index_y = 0, 0

    for column in range(len(matrix[0])):
        count = 0
        for vector in matrix:
            if(vector[column] == element_searched):
                count = count + 1
        if(count > max_count_x):
            max_count_x = count
            index_x = column

    for vector in range(len(matrix)):
        count = 0
        for element in matrix[vector]:
            if(element == element_searched):
                count = count + 1
        if(count > max_count_y):
            max_count_y = count
            index_y = vector

    return index_x, index_y

def matrix_bubble(matrix, element_coordinate, element):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if((x == element_coordinate[0] or y == element_coordinate[1]) and matrix[y][x] == element):
                matrix[y][x] = 'x'

def matrix_general_count(matrix, element):
    count = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if(matrix[row][column] == element):
                count = count + 1

    return count

# Testing
if(__name__ == '__main__'):
    print(f(matrix, 3))
