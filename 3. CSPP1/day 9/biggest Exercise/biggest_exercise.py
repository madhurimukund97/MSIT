'''Exercise : Biggest Exercise'''
#Write a procedure, called biggest, which returns the key
#corresponding to the entry with the largest number of values
#associated with it. If there is more than one such entry,
#return any one of the matching keys.
def biggest(animals):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    flag = 0
    max_1 = ""
    #value = animals.values()
    #result = max(value)
    for keys in animals:
        if len(animals[keys]) > flag:
            flag = len(animals[keys])
            max_1 += keys
        return max_1[-1]
def main():
    '''main'''
    n_1 = input()
    animals = {}
    for _ in range(int(n_1)):
        s_1 = input()
        l_1 = s_1.split()
        if l_1[0][0] not in animals:
            animals[l_1[0][0]] = [l_1[1]]
        else:
            animals[l_1[0][0]].append(l_1[1])
    print(biggest(animals))   
if __name__ == "__main__":
    main()
