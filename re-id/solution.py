# ooookay! Here' we go...
# fun fact, I've actually never written python before... this should be interesting ;-)
# Also, I should go help my kid brush his teeth... but this is intriguing!
# Thanks for the invite :)


# This "naive" solution "works" but it's not very efficient and was failing some tests... so I think it's failing some tests.
# Kept for posterity because "learning" yay!
def naive_solution(i):
	i = int(i)

	# input should be an integer
	if(not isinstance(i,int)):
		raise Exception('Index must be an integer')

	# input should be between 0 and 10000
	if(int(i) < 0 or int(i) > 10000):
		raise Exception('Index must be between 0 and 10000')

	# a list to hold our primes
	primes = []

	# our first prime
	num = 2

	# only compute enough digits to get the index we want (add five to the index since we need 5 digits)
	while len(numList) < (i + 5):
		# all prime numbers are greater than 1
		#is num  divisible by something smaller than me?
		for j in range(2, num):
			if (num % j) == 0:
			#not prime
				break
		else:
			#prime! Add to the list...
			numList.append(num)
	num +=  1

	# smush our list into one long string
	prime_str = ''.join(map(str,primes))

	# slice a 5 digit chunk starting at index i
	slice = list(prime_str)[i:i+5]

	# return it.
	return(''.join(map(str,slice)))


# So I just learned about the "Sieve_of_Eratosthenes" (cool name) 
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# Muuuuch more efficient. Here's my implementation:

def solution(n):	
  # todo: raise errors when "n" is out of bounds (negative or > 10k)
  
  # for some reason, I had to cast this as an int :shrug:
	n = int(n)
	
	#how high do we need to go to get a large enough number of primes?
	#derived via trial and error... :( 
	limit = 20220

	# make a big list of numbers to test
	# assume they're all prime first then "sieve" them out
	primes = [True] * limit

	# zero and 1 aren't prime 
	primes[0] = primes[1] = False

	# loop through our "factors"
	for i in range(2, limit):
		#if a number is still considered prime
		if primes[i]:
			#remove all the numbers which include this prime as a factor (e.g. non-primes)
			for j in range(i + i, limit, i):
				primes[j] = False
	# loop through our table, check if a number is prime (e.g. "true")
  # and add these to a big string
	prime_str = "".join([str(i) for i in range(1, limit) if primes[i]])

	#return the slice we want
	return prime_str[n: n + 5]


#does anybody read these comments? hmmm...
