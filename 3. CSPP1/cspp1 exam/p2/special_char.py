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
    add = ""
    count = 0
    for i in range(length1):
    	print(string1[i])
    	if((string1[i]>='a' and strin1[i]<='z') or (string1[i]>='A' and string1[i]<='Z'))
    		add = add + string1[i]
    	if string1[i]=='!' or string1[i]=='@' or string1[i]=='#' or string1[i]=='$' or string1[i]=='%' or string1[i]=='^' or string1[i]=='&' or string1[i]=='*':
    		add = add + " "


    




if __name__ == "__main__":
    main()
