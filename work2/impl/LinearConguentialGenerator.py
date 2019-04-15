import math, time

# ================ Implementation ================

class LinearCongruentialGenerator:
	def __init__(self, m, a, c, x0):
		"""
		Configure the initial state of the RNG.

		Parameters:
		m  -- The modulus    : m > 0
		a  -- The multiplier : 0 < a < m 
		c  -- The increment  : 0 <= c < m
		x0 -- The seed       : 0 <= x0 < m
		"""
		assert(m > 0)
		assert(0 < a and a < m)
		assert(0 <= c and c < m)
		assert(0 <= x0 and x0 < m)

		self.m  = m
		self.a  = a
		self.c  = c
		self.xi = x0

	def next(self):
		"""
		Generates the next random number.

		Returns:
		The next random number
		"""
		# Generates the next random number with the
		# formula: X(i+1) = (a * X(i) + c) mod m
		self.xi = (self.a * self.xi + self.c) % self.m
		return self.xi

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

def generate(bits, a, c, x0):
	"""
	Builds the RNG and measure the time of generate a random number.

	Parameters:
    bits -- Number of bits expected
	a    -- The multiplier
	c    -- The increment
	x0   -- The seed

    Returns:
    A random number
	"""
	# Calculates the module m of the algorithm
	m = 2 ** bits

	# Init RNG with its arguments
	lcg = LinearCongruentialGenerator(m, a, c, x0)

	# Start measuring time
	start = time.time()

	# Genereates a random number
	number = lcg.next()
	generations = 1

	# While the number does not have sufficient bits
	while not correct_bits_length(bits, number):
		# Genereates a new random number
		number = lcg.next()
		generations += 1

	# Stop measuring time
	end = time.time()

	mean = (end - start) / generations * 1000.0

	# Print the results
	print("Generates a number with %d bits taking %.5f ms:" % (bits, mean))
	print("%d\n" % number)

# ================ Tests ================

if __name__ == '__main__':
	"""
	Main function to execute all random number generations
	"""

	# Default arguments
	a  = 1103515245
	c  = 12345
	x0 = int(time.time())
	bits_array = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

	print("Linear Congruential Generator Parameters:")
	print("a : %d | c: %d | x0: %d | bits: %s\n" % (a, c, x0, str(bits_array)))

	# Execute random number generation
	for bits in bits_array:
		generate(bits, a, c, x0)