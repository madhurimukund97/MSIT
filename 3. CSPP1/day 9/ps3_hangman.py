# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = 0
    for char in range(len(secretWord)):
        if secretWord[char] in lettersGuessed:
            result += 1
    if result == len(secretWord):
        return True
    return False

def Input_test(guess):
    if len(guess) > 1 or (guess >= 'a' and guess <= 'z'):
        print(Invalid)
        return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    list_1 = []
    for char in range(len(secret_word)):
        if secretWord[char] in lettersGuessed:
            list_1.append(secretWord[char])
        else:
            list_1.append('_')
    return ''.join(list_1)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    string_1 = string.ascii_lowercase
    result = ''
    for _ in string_1:
        if _ in lettersGuessed:
            continue
        else:
            result += _
    return ''.join(result)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    letters_guessed = []
    count = 0
    print("I am thinking of a word which is",len(secretWord), "letters word")
    print("-------------")
    
    flag = False
    maxGuessLetters = len(secretWord) + 3
    while maxGuessLetters != 0:
        print("There are ", len(secretWord), "letters long")
        print("You have", maxGuessLetters, "guesses left")
        print("Available letters", getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        maxGuessLetters -= 1
        if not testInput(guess):
            continue
        lettersGuessed.append(guess)
        flag = isWordGuessed(secretWord, lettersGuessed) 
        if flag:
            break
        print(getGuessedWord(secretWord, lettersGuessed))
    if flag:
        print("Congratulations you guessed the correct word")
    else:
        print("Better luck next time")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
    