"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-21 20:23:49
 * @modify date 2020-09-21 21:36:44
 * @desc [
	Solution to: Day 4: Binomial Distribution II
		https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

Binomial mass probability function:

	b(x, n p) = combinations( n | x) * p ** x * q ** (q-x)

	NOTE: combination(n | x)  = n! / x! (n-x)!
 ]
 */
"""

# #########
# Imports
# #########

from typing import Tuple


# #########
# Input
# #########

def get_input() -> Tuple[float, int]:
	"""Returns tuple input from standard in.

	Returns:
		Tuple[float, int]: (% of defective pistons,  size of current batch of pistons)
	"""
	perc_defective_pistons, num_pistons = [int(val) for val in input().split()]
	return (perc_defective_pistons / 100, num_pistons)


# #########
# Mass probability function
# #########

def factorial(n: int) -> int:
	"""Returns factorial of n

	Args:
		n (int): number to take factorial

	Returns:
		int: factorial result
	"""
	output = 1
	for i in range(n, 0, -1):
		output *= i
	return output


def get_mass_prob(x: int, n: int, p: float) -> float:
	"""Returns mass probability function of b(x, n, p)

	Args:
		x (int): number of units
		n (int): total number of units
		p (float): percent chance to reach target

	Returns:
		float: percent chance to return x units out of n
	"""
	q = 1 - p
	combinations = factorial(n) / (factorial(x) * factorial(n-x))
	return combinations * p ** x * q ** (n - x)


def get_cum_prob(lower_limit: int, upper_limit: int, n: int, p: float) -> float:
	"""Returns cumulative probability of returning number between lower & upper limit (inclusive).

	Args:
		lower_limit (int): lower limit of cum probability
		upper_limit (int): upper limit of cum probability
		n (int): total number of trials
		p (float): percent of returning success

	Returns:
		float: cumulative probability to return between lower and upper limit
	"""
	cum_prob = 0
	for i in range(lower_limit, upper_limit + 1):
		cum_prob += get_mass_prob(i, n, p)
	return cum_prob


def format_scale(num: float) -> float:
	"""Returns number formatted to 4 decimal places

	Args:
		num (float): Number to format

	Returns:
		float: Formatted number
	"""
	return "{:.3f}".format(num)


##########
# Main
##########
def main():
	## Input
	percent_dysfunc, pistons = get_input()

	lower, upper = 0, 2
	cum_prob = get_cum_prob(lower, upper, pistons, percent_dysfunc)
	print(format_scale(cum_prob))

	lower, upper = 2, pistons
	cum_prob = get_cum_prob(lower, upper, pistons, percent_dysfunc)
	print(format_scale(cum_prob))


if __name__ == "__main__":
	main()



