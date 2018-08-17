'''
    Document Distance - A detailed description is given in the PDF
'''
import collections
import math
#from collections import Counter
# def frequencyDistribution(data):
#    return {i: data.count(i) for i in data}

def similarity(dict1, dict2):
    

    '''
        Compute the document distance as given in the PDF

    '''
    import string
    #line="a sentence with a few words"
    #line.split()

    #file = open('data.txt', 'r')
    #text = file.read().strip()
    #file.close()
    #for word in words:

        # print the word
    #    print(word)
    #str1 = open('stopwords.txt', 'r').read()

    char1 = string.ascii_letters + ' '
    dict1 = ''.join(f_1 for f_1 in dict1 if f_1 in char1)
    dict2 = ''.join(f_1 for f_1 in dict2 if f_1 in char1)
    dict1 = dict1.lower().strip().split()
    dict2 = dict2.lower().strip().split()
    # print(dict1)
    # print(dict2)

    dicta = load_stopwords("stopwords.txt")
    for word in list(dict1):
        if word in dicta:
            dict1.remove(word)

    for word in list(dict2):
        if word in dicta:
            dict2.remove(word)
    # print(frequencyDistribution(dict1))
    # print(frequencyDistribution(dict2))
    counter1 = collections.Counter(dict1)
    counter2 = collections.Counter(dict2)
    # print(counter1.values())
    # print(counter1)
    # print(counter2)
    '''frequency count'''
    '''from collections import Counter
    list1=['apple','egg','apple','banana','egg','apple']
    counts = Counter(list1)
    print(counts)'''
    dict3 = []
    dict4 = []
    dict5 = []
    for word in counter1:
        if word in counter2:
            dict3.append(counter1[word]*counter2[word])
    

    for word in counter1:
        dict4.append(counter1[word]**2)


    for word in counter2:
        dict5.append(counter2[word]**2)


    return sum(dict3)/(math.sqrt(sum(dict4))*math.sqrt(sum(dict5)))


    #print(dict1, dict2)
    




#def vector_angle(L1,L2):
    # numerator = inner_product(dict1,dict2)
    # denominator = math.sqrt(inner_product(dict1,dict1)*inner_product(dict2,dict2))
    # return math.acos(numerator/denominator)



# def inner_product(dict1,dict2):
#     sum = 0.0
#     for word1, count1 in dict1:
#         for word2, count2 in dict2:
#             if word1 == word2:
#                 sum += count1 * count2
#     return sum

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords1 = []
    with open(filename, 'r') as words:
        for line in words:
            stopwords1.append(line.strip())
    return stopwords1

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
