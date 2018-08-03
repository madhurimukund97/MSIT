'''Write a python program to find the square root of the given number'''
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    #s = raw_input()
    # epsilon and step are initialized
    # don't change these values
    '''approximation method'''
    number = int(input())
    epsilon = 0.01
    step = 0.0
    add = 0.1
    while abs(step**2-number) >= epsilon:
        step += add
    if abs(step**2 - number) >= epsilon:
        print("Failed on square root of", number)
    else:
        print(step)
    # your code starts here

if __name__ == "__main__":
    main()
