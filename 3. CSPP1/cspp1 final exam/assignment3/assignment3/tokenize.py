'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
# import collections
# def frequencydistribution(data):
#     '''frequency distribution'''
#     return {i: data.count(i) for i in data}

def tokenize(string):
    #char1 = string.ascii_letters + ' '
    dict = {}
    for index in string:
        # for jindex in index:
        if index not in dict:
            dict[index] = 0
        else:
            dict[index] += 1
    return dict
  
def main():
    input1 = ''
    num = int(input())
    for i in range(num):
        i += 1
        input1 += input()
        #input1 += '\n'
    input2 = tokenize(input1)
    print(input2)


if __name__ == '__main__':
    main()
