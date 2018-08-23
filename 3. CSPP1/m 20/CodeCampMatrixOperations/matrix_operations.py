def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    mult = copy.deepcopy(m1)
    for ind in range(0, len(m1), 1):
        for jind in range(0, len(m2[0]),1):
            mult[ind][jind] = 0
            for kind in range(0, len(m2), 1):
                mult[ind][jind] = int(mult[ind][jind])
                mult[ind][jind] += int(m1[ind][kind]) * int(m2[kind][jind])
    return mult
    

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    sum1 = copy.deepcopy(m1)
    if len(m1) == len(m2):
        for ind in range(len(m1)):
            for jind in range(len(m2)):
                result = int(sum1[ind][jind])
                result += int(m2[ind][jind])
                sum1[ind][jind] = result
        return sum1
    else:
        print("Error: Matrix shapes invalid for addition")
        print("None")
    

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows = int(size[0])
    cols = int(size[1])
    res = 0
    list1 = []
    for ind in range(0, rows, 1):
        row = input().split()
        list1.append(row)
        res += len(row)
    if res != rows * cols:
        print("Error: Invalid input for the matrix")
    else:
        return list1


def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    num1 = input().split(',')
    matrix1 = read_matrix(num1)
    num2 = input().split(',')
    matrix2 = read_matrix(num2)

if __name__ == '__main__':
    main()
