'''Exercise: eval quadratic'''

# Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic
#a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.


def quadratic_equation(a_1, b_1, c_1, x_1):
    '''eval quadratic'''
    return a_1*x_1**2+b_1*x_1+c_1

def main():
    '''quadratic'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for _ in enumerate(data):
        temp = str(data[_]).split('.')
        if temp[1] == '0':
            data[_] = int(float(str(data[_])))
        else:
            data[_] = data[_]
    print(quadratic_equation(data[0], data[1], data[2], data[3]))
if __name__ == "__main__":
    main()
