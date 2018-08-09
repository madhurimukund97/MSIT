'''Exercise : Function and Objects Exercise-3'''
#Implement a function that converts the given
#testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(L):
    return L*L
def apply_to_each(L, f):
    '''to each'''
    z = map(square, L)
    print(list(z))
    
    
def main():
    '''main'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    apply_to_each(list1, square)

if __name__ == "__main__":
    main()