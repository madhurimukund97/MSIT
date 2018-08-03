'''Write a python program to find if the given number is a perfect cube or not'''
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    '''guess and check method'''
    # input is captured in s
    #s = raw_input()
    # watch out for the data type of value stored in s
    # your code starts here
    number = int(input())
    count = 0
    while count**3 < number:
        count += 1
    if count**3 != number:
        print(str(number), 'is not a perfect cube')
    else:
        print(str(number), 'is a perfect cube')
if __name__ == "__main__":
    main()
