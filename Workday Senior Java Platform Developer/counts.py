import math


# Returns sum of all factors
# of n. 
def sumofoddFactors(n):
	# Traversing through all
	# prime factors.
	res = 1

	# ignore even factors by
	# of 2
	while n % 2 == 0:
		n = n // 2

	for i in range(3, int(math.sqrt(n) + 1)):

		# While i divides n, print
		# i and divide n
		count = 0
		curr_sum = 1
		curr_term = 1
		while n % i == 0:
			count += 1

			n = n // i
			curr_term *= i
			curr_sum += curr_term

		res *= curr_sum

	# This condition is to
	# handle the case when
	# n is a prime number.
	if n >= 2:
		res *= (1 + n)

	return res


def counts(numbers):
	results = 0
	for num in numbers:
		results += sumofoddFactors(num)
	return results
