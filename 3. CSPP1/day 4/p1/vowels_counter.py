'''Assume s is a string of lower case characters.'''

#Write a program that counts up the number of vowels
#contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    '''vowels'''
    #s = raw_input()
    # the input string is in s
    # remove pass and start your code here
    string = input()
    count = 0
    for char in string:
        if char in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    print(str(count))
if __name__ == "__main__":
    main()
