'''Exercise : how many'''
# write a procedure, called how_many, which returns
#the sum of the number of values associated with a dictionary.


def how_many(animals):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    sum1 = 0
    value = animals.values()
    for list_1 in value:
        sum1 += len(list_1)
    return sum1
def main():

    '''animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')'''
    n_1 = input()
    animals = {}
    for _ in range(int(n_1)):
        s_1 = input()
        l_1 = s_1.split()
        if l_1[0][0] not in animals:
            animals[l_1[0][0]] = [l_1[1]]
        else:
            animals[l_1[0][0]].append(l_1[1])
    print(animals)
    print(how_many(animals))
if __name__ == "__main__":
    main()
