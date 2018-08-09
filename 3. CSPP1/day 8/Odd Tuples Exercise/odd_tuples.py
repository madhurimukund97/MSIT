'''Exercise : Odd Tuples'''
#Write a python function oddTuples(aTup) that takes a some numbers
#in the tuple as input and returns a tuple in which contains
#odd index values in the input tuple
def odd_tuples(a_tup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    #aTup = ('I', 'am', 'a', 'test', 'tuple')
    j_1 = ()
    for i_1 in range(0, len(a_tup), 2):
        j_1 += (a_tup[i_1],)
    return j_1
    #return aTup[0::2]
    #z= tuple((t[i] for i_1 in range(0, len(a_tup), 2)))
    #print(z)
    
def main():
    '''main'''
    data = input()
    data = data.split()
    a_tup = ()
    for j in enumerate(data):
        a_tup += (int(data[j]),)
    print(odd_tuples(a_tup))
if __name__ == "__main__":
    main()
