'''Exercise : Function and Objects Exercise-1'''
#Implement a function that converts the given
#testList = [1, -4, 8, -9] into [1, 4, 8, 9]

def apply_to_each(test_list, f):
    '''apply to each'''
    '''l1 = [1, 1, 2 ,3]
    l2 = [2, 4, 6, 88]
    z = map(min, l1, l2)
    print(list(z))'''
    #apply_to_each(list1, abs)
    #z_1 = map(abs, test_list)
    return(list(map(abs, test_list)))

def main():
    '''main'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
