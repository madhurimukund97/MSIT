#define the gen_primes function here
def genPrimes():
    primes = [2]
    yield primes[0]
    guess = 3
    while True:
        if all(guess%x != 0 for x in primes):
            primes.append(guess)        
        if guess == primes[-1]:
            yield primes[-1]
        guess += 2

def main():
	data=input()
	l=data.split()
	a=int(l[0])
	b=int(l[1])
	primeGenerator = genPrimes()
	for i in range(a):
	    p=primeGenerator.next()
	    if(i%b==0):
	        print(p)
	
if __name__== "__main__":
	main()
