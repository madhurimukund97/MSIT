'''
Write a function to clean up a given string by removing the special
characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(text):
    '''clean a string'''
    for letters in text:
        text = re.sub('[^A-Za-z0-9]+', '', letters)
        print(text, end='')
    return text
def main():
    '''main'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
