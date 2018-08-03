'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''newton raphson method'''
    #s = raw_input()
    # epsilon and step are initialized
    # don't change these values
    epsilon = 0.01
    # your code starts here
    number = int(input())
    random = number/2.0
    while abs(random*random-number) >= epsilon:
        random = random - (((random**2) - number)/(2*random))
    print(random)

if __name__ == "__main__":
    main()
