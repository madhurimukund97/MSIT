'''Exercise: Assignment-1'''
# Write a Python function, factorial(n),
#that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(num):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    temp = num
    if temp == 0:
        return 1
    if num == 1:
        return num
    return num * factorial(num-1)
def main():
    '''main'''
    a_1 = input()
    print(factorial(int(a_1)))

if __name__ == "__main__":
    main()
