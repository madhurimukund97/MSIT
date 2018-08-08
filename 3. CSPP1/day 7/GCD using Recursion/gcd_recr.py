'''Exercise: GCDRecr'''
# Write a Python function, gcdRecur(a, b), that takes in two numbers
#and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcd_recur(first, second):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if second == 0:
        return first
    else:
        return gcd_recur(second, first%second)
def main():
    '''main'''
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
