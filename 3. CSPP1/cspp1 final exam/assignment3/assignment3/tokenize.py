'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
# import collections
def frequencydistribution(data):
    '''frequency distribution'''
    return {i: data.count(i) for i in data}

def tokenize(string):
    #char1 = string.ascii_letters + ' '
    string = string.split()
    print(string)
    string = ''.join(f_1 for f_1 in string if f_1 in char1)
    print(string)
    # for word in list(string):
    counter1 = frequencydistribution(string)
    print(counter1)






    
def main():
    # n=input()
    # adict={}
    # for i in range(int(n)):
    #     data=input()
    #     l=data.split()
    #     adict[l[0]]=int(l[1])
    # data1=input()
    # print(updateHand(adict,data1))
    input1 = ''
    num = int(input())
    for i in range(num):
        i += 1
        input1 += input()
        input1 += '\n'
    print(input1)


if __name__ == '__main__':
    main()
