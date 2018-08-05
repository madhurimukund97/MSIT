'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    #str_input = input()
    string1 = input()
    length1 = len(string1)
    print(length1)
    string2 = ""
    count = 0
    i=0
    while(count>length1):
    	for i in range(string1):
    		print(string1[i])
    		count+=1
    '''for char in string1:
    	print(char, end="")'''


    




if __name__ == "__main__":
    main()
