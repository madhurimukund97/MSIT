'''Assume s is a string of lower case characters.'''

#Write a program that prints the longest substring of s
#in which the letters occur in alphabetical order.
#For example, if s = 'azcbobobegghakl', then your program should print

#Longest substring in alphabetical order is: beggh

#In the case of ties, print the first substring.
#For example, if s = 'abcbcd', then your program should print

#Longest substring in alphabetical order is: abc

#Note: This problem may be challenging. We encourage you to work smart.
#If you've spent more than a few hours on this problem,
#we suggest that you move on to a different part of the course.
#If you have time, come back to this problem after
#you've had a break and cleared your head.

def main():
    '''longest substring'''
    #s = raw_input()
    # the input string is in s
    # remove pass and start your code here
    string = input()
    maxstring = ""
    length = len(string)
    for j in range(length):
        substr = ""
        temp = string[j]
        for i in range(j, len(string)):
            if temp <= string[i]:
                temp = string[i]
                substr += temp
            else:
                break
        if len(maxstring) < len(substr):
            maxstring = substr
    print(maxstring)
if __name__ == "__main__":
    main()
