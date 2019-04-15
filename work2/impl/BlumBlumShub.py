import math, time

# ================ Implementation ================

class BlumBlumShub:
	def __init__(self, n, seed, bits_amount):
		"""
		Configure the initial state of the RNG.

		Parameters:
		n            -- n = p * q where (p mod 4) = (q mod 4) = 3
		seed         -- Initial value
		bits_amount  -- Size of the bitstream for generate a number
		"""
		self.n = n
		self.bits_amount = bits_amount
		self.xi = pow(seed, 2, n)

	def next(self):
		"""
		Generates the next random number.
		"""
		# Bitstream
		bitstream = ""

		# Generates a stream with size equal bits amount
		for bits in range(0, self.bits_amount):

			# Calculates: X(i+1) = X(i)^2 % n
			self.xi = pow(self.xi, 2, self.n)

			# Gets the least bit significant
			bit_i = self.xi % 2

			# Concatenates the new bit on bitstream
			bitstream = bitstream + str(bit_i)
		
		# Converts bitstream into integer with bits amount of length
		return int(bitstream, 2)

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

def generate(n, seed, bits):
	"""
	Builds the RNG and measure the time of generate a random number.

	Parameters:
	n            -- n = p * q where (p mod 4) = (q mod 4) = 3
	seed         -- Initial value
	bits_amount  -- Size of the bitstream for generate a number
	"""
	# Init RNG with its arguments
	bbs = BlumBlumShub(n, seed, bits)

	# Start measuring time
	start = time.time()

	# Genereates a random number
	number = bbs.next()
	generations = 1

	# While the number does not have sufficient bits
	while not correct_bits_length(bits, number):
		# Genereates a new random number
		number = bbs.next()
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
	n    = 192649
	seed = 101355
	bits_array = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

	print("BlumBlumShub Parameters: n=%d, seed=%d, bits=%s\n" % (n, seed, str(bits_array)))

	# Execute random number generation
	for bits in bits_array:
		generate(n, seed, bits)
