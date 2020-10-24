"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-22 11:27:05
 * @modify date 2020-09-22 11:27:05
 * @desc [
	Solution to: Day 4: Geometric Distribution II
		https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
 
The probability that a machine produces a defective product is 1/3. 
What is the probability that the 1st defect is found during the first 5 inspections?

Because the geometric probability function calculates the mass probability for a single inspection,
I will use a summation of the geom_prob() formula.

-----
NOTE: A second method that avoids computational heavy summations is to find the probability that the first 5 did NOT
have any defects.

Because triasl are independent, we can use calculate this by finding the complement of the success rate to the power of n
	= 1 - (1 - 1/3) ** 5
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
	"""Return input for Day 4: Geom Dist II.

	Returns:
		Tuple[float, int]: p and n, respectively
	"""
	num, denom = [int(x) for x in input().split()]
	p = num/denom
	n = int(input())
	return (p, n)


# #########
# Geometric Distribution
# #########

def calc_geom_dist(n: int, p: float) -> float:
	"""Returns probability mass of geom distribution for n, p

	Args:
		n (int): number of trials
		p (float): p(x)

	Returns:
		float: Probability of geom dist given n, p
	"""
	q = 1 - p
	return q ** (n-1) * p


def get_cum_geom_prob(n: int, p: float) -> float:
	"""Returns cumulative probability of geometric distribution in n trials

	Args:
		n (int): total number of trials
		p (float): P(x)

	Returns:
		float: Cumulative probability of x in n trials
	"""
	cum_prob = 0

	for i in range(1, n + 1):
		geom_prob = calc_geom_dist(i, p)
		cum_prob += geom_prob
	return cum_prob


# #########
# Format
# #########

def format_scale(num: float) -> float:
	"""Returns number with decimals formatted to scale

	Args:
		num (float): Number to format

	Returns:
		float: Number formatted to scale
	"""
	return f'{num:.3f}'


# #########
# Main
# #########

def main():
	p, n = get_input()

	cum_prob = get_cum_geom_prob(n, p)
	print(format_scale(cum_prob))


if __name__ == "__main__":
	main()

