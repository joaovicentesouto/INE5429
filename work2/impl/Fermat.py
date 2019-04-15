import math, time
from RandomNumberGenerators import LinearCongruentialGenerators

# ================ Implementation ================

def Fermat(n, k, rng):
	# Ignore some cases
	if n < 2 or n % 2 == 0:
		return "conclusive"

	# Repeat k times
	for _ in range(k):

		# Generates a into [2, n-2]
		a = (generate(rng) % n - 3) + 2

		# Calculate a^(n-1) % n and if is different of 1 then n is not prime
		if pow(a, n - 1, n) != 1:
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

	print("Fermat with Linear Congruential Generators (%d iterations)\n" % iterations)

	for bits in bits_array:
		number = 0
		attempts = 0
		is_prime = False
		rng = LinearCongruentialGenerators(2 ** bits, 25214903917, 11, int(time.time()))

		start = time.time()

		while not is_prime:

			attempts+= 1
			is_prime = True
			number = generate(rng)

			is_prime = Fermat(number, iterations, rng) == "probably prime"

		end = time.time()

		final_time = (end - start) * 1000.0

		print("Bits %d: took %d attempts and took %.5f ms to find the follow prime number:" % (bits, attempts, final_time))
		print("%d\n" % number)
