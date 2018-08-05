'''Guess My Number Exercise'''

def main():
    #s = raw_input()
    #your code here
    '''guess number'''
    mid = 50
    last = 100
    first = 0
    input1 = 'l'
    while input1 != 'c':
        print(mid)
        input1 = input("Enter 'h' if guess is too high, 'l' if its too low.\
                        'c' to indicate I guessed correctly")
        if input1 == 'h':
            last = mid
            mid = (last + first) // 2
        elif input1 == 'l':
            first = mid
            mid = (last + first) // 2
    print('your guess number is :', mid)
if __name__ == "__main__":
    main()
