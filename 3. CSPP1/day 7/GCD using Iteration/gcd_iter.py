'''Exercise: GCDIter'''
# Write a Python function, gcdIter(a, b), that takes in two numbers
#and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcd_iter(first, second):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if first > second:
        small = second
    else:
        small = first
    for i in range(1, small+1):
        if (first % i == 0) and (second % i == 0):
            gcd = i
    return gcd
def main():
    '''main'''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
