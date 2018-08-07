'''Exercise: fourth power'''

# Write a Python function, fourthPower, that takes in one number
#and returns that value raised to the fourth power.

# You should use the square procedure that you defined in an earlier
#exercise exercise (you don't need to redefine square in this box;

# This function takes in one number and returns one number.

def square(x_1):
    '''
    x: int or float.
    '''
    # Your code here
    return x_1*x_1
def fourth_power(x_1):
    '''
    x: int or float.
    '''
    # Your code here
    result = square(x_1)
    return result * result
def main():
    '''main'''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourth_power(int(float(str(data)))))
    else:
        print(fourth_power(data))
if __name__ == "__main__":
    main()
