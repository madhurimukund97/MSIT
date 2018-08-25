'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''main'''
    input1 = ''
    num = int(input())
    for i in range(num):
        i += 1
        input1 += input()
        input1 += '\n'
    print(input1)
if __name__ == '__main__':
    main()
