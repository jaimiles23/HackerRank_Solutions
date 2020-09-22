	"""/**
	* @author [Jai Miles]
	* @email [jaimiles23@gmail.com]
	* @create date 2020-09-22 10:35:01
	* @modify date 2020-09-22 10:35:01
	* @desc [
		Solution to: Day 4: Geometric Distribution I
			https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

	This script contains 3 sections:
		1. Notes on Geometric distributions
		2. Math solution 
		2. Python solution 


	##########
	# Notes
	##########

	## Negative Binomial Experiment
	The negative binomial experiment has the following properties:
		- n, independent trials
		- binary outcome:success (s), or failure (f)
		- P(s) is the same for every trial
		- experiment continues until `x` successes are observed.

	If X is the number of experiments until the `x`th success, then X is a discrete random variable called a negative binomial.


	## Negative Binomial Distribution
	Consider the following probability mass function
		b*(x, n, p) = (n - 1 | x - 1) * p ** x * q ** (n-x)

	This is a negative binomial with the following properties:
		- number of successes to be observed is x
		- n, number of trials
		- p, p(x) in 1 trial
		- q, p( not x) in 1 trial
		- b*(x, n, p) is the negative binomial probability, MEANING: the probability of having x - 1 successes after n - 1 trials and 
		having x successes after n trials


	## Geometric Distribution
	Geometric distribution is the special case of a negative binomial distribution to determine the number of Bernoulli trials required for a success.
	Recall, X is the number of successes in n independent trials, so for each i, 1 <= i <= n
		X(i) = 1: if the i-th trial is a success, 0 otherwise

	The geometric distribution is a negative binomial distribution where the number of successes is 1. We express this with the following formula:
	g(n, p) = q ** (n - 1) * p


	## Example:
	Bob is a high school basketball player. He is a 70% free throw shooter, meaning his probability of making a free throw is 0.70. 
	What is the probability that Bob makes his first free throw on his fifth shot?


	For this experiment, n = 5, p = 0.7 and q = 0.3, So,
		g(5, 0.7) = 0.3 ** 4 * 0.7
			= 0.00567


	##########
	# Math Solution
	##########

	The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the 5th inspection?

	n = 5
	p = 1/3
	q = 2/3

		g(n, p) = q ** (n - 1) * p
			= 2/3 ** (4) * 1/3
				= 0.0082
	]
	*/
	"""

	##########
	# Imports
	##########

	from typing import Tuple


	##########
	# Input
	##########

	def get_input() -> Tuple[float, int]:
		"""Returns input for Day 4: Geometric distribution i.

		Returns:
			Tuple[float, int]: Geometric distribution p and n, respectively
		"""
		num, denom = [int(x) for x in input().split()]
		p = num / denom
		n = int(input())
		return (p, n)


	##########
	# Geometric Distribution
	##########

	def calc_geom_dist(n: int, p: float) -> float:
		"""Returns geometric distribution of n & p

		g(n, p) = q ** (n-1) * p

		Args:
			n (int): number of trials
			p (float): probability of x

		Returns:
			float: Geometric distribution, given n and p
		"""
		q = 1 - p
		return q ** (n-1) * p


	##########
	# Scaler
	##########

	def format_scale(num: float) -> float:
		"""Returns number formatted to scale

		Args:
			num (float): Number to format

		Returns:
			float: Number formatted to scale
		"""
		return "{:.3f}".format(num)



	##########
	# Main
	##########

	def main():
		p, n = get_input()

		geom_dist = calc_geom_dist(n, p)
		print( format_scale(geom_dist))


	if __name__ == "__main__":
		main()
