'''mult matrix'''
import copy
def mult_matrix(m_1, m_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m_1) != len(m_2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None
    _ = copy.deepcopy(m_1)
    mat = []
    for i in range(len(m_1)):
        mat1 = []
        for j in range(len(m_2[0])):
            mult = 0
            for k in range(len(m_2)):
                mult += m_1[i][k] * m_2[k][j]
            mat1.append(mult)
        mat.append(mat1)
    return mat

def add_matrix(m_1, m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m_1) != len(m_2):
        print("Error: Matrix shapes invalid for addition")
        return None
    matrix = copy.deepcopy(m_1)
    for i in range(len(m_1)):
        for j in range(len(m_1[0])):
            matrix[i][j] = m_1[i][j] + m_2[i][j]
    return matrix
def read_matrix(size):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    for index in range(size[0]):
        mat1 = input()
        mat1 = list(map(int, mat1.split(' ')))
        matrix.append(mat1)
    if size[0] != len(matrix):
        return None
    for index in matrix:
        if len(index) != size[1]:
            return None
    return matrix

def main():
    '''main'''
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    size1 = input()
    size1 = list(map(int, size1.split(',')))
    matrix2 = read_matrix(size1)
    size2 = input()
    size2 = list(map(int, size2.split(',')))
    matrix3 = read_matrix(size2)
    if matrix2 == None or matrix3 == None:
        print("Error: Invalid input for the matrix")
    else:
        add = add_matrix(matrix2, matrix3)
        print(add)
        mul = mult_matrix(matrix2, matrix3)
        print(mul)

if __name__ == '__main__':
    main()
