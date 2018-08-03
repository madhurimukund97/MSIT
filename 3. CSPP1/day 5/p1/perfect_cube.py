'''Write a python program to find if the given number is a perfect cube or not'''
# using guess and check algorithm

def main():
    '''perfect cube or not'''
    #s = raw_input()
    #your code here
    number = int(input())
    guess = 0
    while guess**3 < abs(number):
        guess = guess + 1
    if guess**3 != abs(number):
        print(str(number) + 'is not a perfect cube')
    else:
        if number < 0:
            guess = -guess
        print(str(number) + 'is a perfect cube')

if __name__ == "__main__":
    main()
