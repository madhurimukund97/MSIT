'''Exercise: Integer Division Exercise'''
#Modify the code for integer_division so that this error does not occur.

def integer_division(x_1, a_1):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x_1 >= a_1:
        count += 1
        x_1 = x_1 - a_1
    return count
def main():
    '''main'''
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
