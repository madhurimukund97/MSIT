'''Exercise: Assignment-2'''
# Write a Python function, sumofdigits,
#that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(num):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    temp = num
    temp = num
    if temp == 0:
        return 0
    if num == 1:
        return 1
    return (num%10) + sumofdigits(num//10)
def main():
    '''main'''
    a_1 = input()
    print(sumofdigits(int(a_1)))

if __name__ == "__main__":
    main()
