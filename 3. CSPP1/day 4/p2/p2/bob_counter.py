'''Assume s is a string of lower case characters.'''

#Write a program that prints the number of times
#the string 'bob' occurs in s. For example,
#if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2'''

def main():
    '''bob count'''
    #s = raw_input()
    # the input string is in s
    # remove pass and start your code here
    string = input("string=")
    count = 0
    sub_len = len('bob')
    for i in range(len(string)):
        if string[i:i+sub_len] == 'bob':
            count += 1
    print(count)
if __name__ == "__main__":
    main()
