#define the gen_primes function here
def is_prime(num):
	for index in range(2, num):
		if num%index == 0:
			return False
	return True
def genPrimes():
    num1 = 2
    while True:
    	if is_prime(num1):
    		yield num1
    	num1 += 1
def main():
	data=input()
	l=data.split()
	a=int(l[0])
	b=int(l[1])
	primeGenerator = genPrimes()
	for i in range(a):
	    p=primeGenerator.__next__()
	    if(i%b==0):
	        print(p)
	
if __name__== "__main__":
	main()
