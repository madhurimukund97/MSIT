'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''bisection method'''
    #s = raw_input()
    # epsilon and step are initialized
    # don't change these values
    number = int(input())
    epsilon = 0.01
    first = 0.0
    last = number
    mid = (first+last)/2.0
    while abs(mid**2 - number) >= epsilon:
        if mid**2 < number:
            first = mid
        else:
            last = mid
        mid = (last+first)/2
    print(mid)
    # your code starts here

if __name__ == "__main__":
    main()
