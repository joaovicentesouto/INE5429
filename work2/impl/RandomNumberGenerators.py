class LinearCongruentialGenerators:
	def __init__(self, m, a, c, x0):
		self.m  = m
		self.a  = a
		self.c  = c
		self.xi = x0

	def next(self):
		self.xi = (self.a * self.xi + self.c) % self.m
		return self.xi

class BlumBlumShub:
	def __init__(self, n, seed, bits_amount):
		self.n = n
		self.seed = seed
		self.bits_amount = bits_amount
		self.xi = (seed ** 2) % n

	def next(self):
		bitstream = ""
		for bits in range(0, self.bits_amount):
			self.xi = pow(self.xi, 2, self.n)
			bit_i = self.xi % 2
			bitstream = bitstream + str(bit_i)
		return int(bitstream, 2)
