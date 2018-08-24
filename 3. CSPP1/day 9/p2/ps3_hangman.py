'''Hangman game'''
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME = "words.txt"

def loadwords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    infile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = infile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseword(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

#end of helper code
#-----------------------------------

#Load the list of words into the variable wordlist
#so that it can be accessed from anywhere in the program
wordlist = loadwords()

def iswordguessed(secretword, lettersguessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = 0
    for char in secretword:
        if char in lettersguessed:
            result += 1
    if result == len(secretword):
        return True
    return False

def inputtest(guess):
    '''input test'''
    if len(guess) > 1 or (guess <= 'a' and guess >= 'z'):
        print("Invalid")
        return False
    return True

def getguessedword(secretword, lettersguessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    list_1 = []
    for char in range(len(secretword)):
        if secretword[char] in lettersguessed:
            list_1.append(secretword[char])
        else:
            list_1.append('_')
    return ''.join(list_1)



def getavailableletters(lettersguessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    string_1 = string.ascii_lowercase
    result = ''
    for char in string_1:
        if char in lettersguessed:
            continue
        else:
            result += char
    return ''.join(result)
def hangman(secretword):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    *At the start of the game, let the user know how many
    letters the secretWord contains.

    *Ask the user to supply one guess (i.e. letter) per round.

    *The user should receive feedback immediately after each guess
    about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
    partially guessed word so far, as well as letters that the
    user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lettersguessed = []
    print("I am thinking of a word which is", len(secretword), "letters word")
    print("-------------")
    flag = False
    maxguessletters = len(secretword) + 7
    while maxguessletters != 0:
        #print("There are ", len(secretword), "letters long")
        print("You have", maxguessletters, "guesses left")
        print("Available letters", getavailableletters(lettersguessed))
        guess = input("Please guess a letter: ")
        maxguessletters -= 1
        if not inputtest(guess):
            continue
        lettersguessed.append(guess)
        flag = iswordguessed(secretword, lettersguessed)
        if flag:
            break
        print(getguessedword(secretword, lettersguessed))
    if flag:
        print("Congratulations you guessed the correct word")
    else:
        print("Better luck next time")
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretword = chooseword(wordlist).lower()
hangman(secretword)
