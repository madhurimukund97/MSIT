#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. This function allows the user to play out a single hand. First, though, you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    len = 0
    for letter in hand.keys():
        len += hand.get(letter, 0)
    return len
def main():
	n=input()
	adict={}
	for i in range(int(n)):
		data=input()
		l=data.split()
		adict[l[0]]=int(l[1])
	print(calculateHandlen(adict))
if __name__== "__main__":
	main()
