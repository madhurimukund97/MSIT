'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
def sort(hand):
    length1 = len(hand)
    newhand = []
    for i in range(length1):
        if hand[i][0] == 'T':
            newhand.append(10)
        elif hand[i][0] == 'J':
            newhand.append(11)
        elif hand[i][0] == 'Q':
            newhand.append(12)
        elif hand[i][0] == 'K':
            newhand.append(13)
        elif hand[i][0] == 'A':
            newhand.append(14)
        else:
            newhand.append(int(hand[i][0]))
    return newhand
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    #return len(set(lst)) == len(lst) and max(lst) - min(lst) == len(lst) - 1
    #list1 = ["T=10", "J=11", "Q=12", "K=13", "A=14"]
    #len1 = len(hand)
    length1 = len(hand)
    sorlst = sorted(sort(hand))
    for i in range(length1-1):
        if sorlst[i+1] -sorlst[i] != 1:
            return False
    return True

    '''s=s


    '''
def four_of_kind(hand):
    count = 0
    sorlst = sorted(sort(hand))
    for i in range(len(sorlst)-3):
        if sorlst[i] == sorlst[i+1] == sorlst[i+2] == sorlst[i+3]:
            count += 1
    if count == 1:
        return True
    return False

def three_of_kind(hand):
    count = 0
    sorlst = sorted(sort(hand))
    for i in range(len(sorlst)-2):
        if sorlst[i] == sorlst[i+1] == sorlst[i+2]:
            count += 1
    if count == 1:
        return True
    return False
def one_pair(hand):
    sorlst = sorted(sort(hand))
    setlst = set(sorlst)
    if len(sorlst) - len(setlst) == 1:
        return True
    return False
def two_pair(hand):
    sorlst = sorted(sort(hand))
    setlst = set(sorlst)
    if len(sorlst) - len(setlst) == 2:
        return True
    return False
def full_house(hand):
    count = 0
    i = 0
    sorlst = sorted(sort(hand))
    if sorlst[i] == sorlst[i+1] == sorlst[i+2] or sorlst[i+3] == sorlst[i+4]:
        count += 1
    elif sorlst[i+3] == sorlst[i+4] and sorlst[i] == sorlst[i+1] == sorlst[i+2]:
        count += 1
    if count == 1:
        return True
    return False


def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    length1 = len(hand)
    for i in range(length1 - 1):
        if hand[i][1] != hand[i+1][1]:
            return False
    return True
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if three_of_kind(hand):
        return 3
    if one_pair(hand):
        return 1
    if two_pair(hand):
        return2
    if full_house(hand):
        return 7
    if four_of_kind(hand):
        return 4
    if is_flush(hand) and is_straight(hand):
        return 8
    if is_straight(hand):
        return 6
    if is_flush(hand):
        return 5

    return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
