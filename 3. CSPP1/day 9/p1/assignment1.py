'''Exercise : Assignment-1'''
#implement the function get_available_letters that takes in one parameter -
#a list of letters, letters_guessed. This function returns a string
#that is comprised of lowercase English letters -
#all lowercase English letters
#that are not in letters_guessed
import string
def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents
    what letters have not
      yet been guessed.
    '''
    string_1 = string.ascii_lowercase
    result = ''
    for _ in string_1:
        if _ in letters_guessed:
            continue
        else:
            result += _
    return ''.join(result)
def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))
if __name__ == "__main__":
    main()
