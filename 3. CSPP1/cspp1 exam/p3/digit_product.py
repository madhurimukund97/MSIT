'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    num = int(input())
    mul = 1
    temp = num
    if num < 0:
        num = -num
    elif num == 0:
        mul = 0
    while num != 0:
        rem = num%10
        mul = mul*rem
        num = num//10
    if temp < 0:
        mul = -mul
    print(mul)
if __name__ == "__main__":
    main()
