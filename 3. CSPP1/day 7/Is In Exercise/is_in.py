'''Exercise: Is In'''
# Write a Python function, isIn(char, aStr),
#that takes in two arguments a character and String
#and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character
#and String and returns one boolean value.

def is_in(char, str1):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    result = 0
    length = len(str1)
    if result == length:
        return False
    if char == str1[result]:
        return True
    str1 = str1[result + 1 : length]
    return is_in(char, str1)

def main():
    '''main'''
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))
if __name__ == "__main__":
    main()
