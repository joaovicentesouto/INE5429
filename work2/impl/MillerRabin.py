import math, time
from RandomNumberGenerators import LinearCongruentialGenerators

# ================ Implementation ================

def MillerRabin(n, k, rng):
	# Ignore some cases
	if n < 4 or n % 2 == 0:
		return "conclusive"

	# Write n as (2^r * d) + 1 with d odd (by factoring out powers of 2 from n − 1)
	d = n-1
	r = 0
	while d % 2 == 0:
		d = d >> 1
		r += 1

	# Repeat k times:
	for _ in range(k):
		
		# Pick a random integer a in the range [2, n − 2]
		a = (generate(rng) % n - 3) + 2

		# a^d % m
		x = pow(a, d, n)

		# With that a, is inconclusive
		if x == 1 or x == n-1:
			continue

		conclusive = True
		for _ in range(r - 1):

			# x(i+1) = x(i)^2 % n
			x = pow(x, 2, n)

			# inconclusive
			if x == n - 1:
				conclusive = False
				continue
		
		# If this a is inconclusive then repeat the process
		if conclusive:
			return "conclusive"
	
	return "probably prime"

# ================ Auxiliar functions ================

def correct_bits_length(bits_expected, number):
	"""
	Checks if the number has sufficient bits

	Keyword arguments:
	bits_expected -- Number of bits expected. 
	number        -- Decimal number

	Returns:
	True if equal False otherwise
	"""
	length_expected = int(math.log10(2 ** bits_expected))
	actual_length = int(math.log10(number))
	return length_expected == actual_length

def generate(rng):
	"""
	Builds the RNG and measure the time of generate a random number.

	Parameters:
	rng -- RNG

    Returns:
    A random number
	"""
	# Genereates a random number
	number = rng.next()

	# While the number does not have sufficient bits
	while not correct_bits_length(bits, number):
		# Genereates a new random number
		number = rng.next()
	
	return number

# ================ Tests ================

if __name__ == '__main__':

	iterations = 100
	bits_array = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

	print("MillerRabin with Linear Congruential Generators (%d iterations)\n" % iterations)

	# For any amount of bits
	for bits in bits_array:
		number = 0
		attempts = 0
		is_prime = False

		# Use LCG as RNG
		rng = LinearCongruentialGenerators(2 ** bits, 25214903917, 11, int(time.time()))

		# Start measuring time
		start = time.time()

		# While the number is not prime
		while not is_prime:

			# Attempts counter
			attempts+= 1
			is_prime = True

			# Generates a random number
			number = generate(rng)

			# Checks if is probably a prime number
			is_prime = MillerRabin(number, iterations, rng) == "probably prime"

		# Stop measuring time
		end = time.time()

		final_time = (end - start) * 1000.0

		print("Bits %d: took %d attempts and took %.5f ms to find the follow prime number:" % (bits, attempts, final_time))
		print("%d\n" % number)
