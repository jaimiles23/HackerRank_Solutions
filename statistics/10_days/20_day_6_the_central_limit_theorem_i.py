# -*- coding: utf-8 -*-
"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-25 17:20:05
 * @modify date 2020-09-25 17:20:05
 * @desc [
	Solution to: Day 6: The Central Limit Theorem I
		https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

This script contains 2 sections:
	1. Tutorial Notes
	2. Python Solution

##########
# Central Limit Theorem
##########

Given a large enough Sample, N, the distribution of the sample mean will approach normal distribution. 
This holds for a sample of random variables with a finite standard deviation.




Let {X1, X2, X3 ... Xn} be a random data set of size n, that is, a sequence of independent and identically distributed 
random variables drawn from distributions of expected values given by µ and finite variances given by σ². 
The sample average is:

	sn = SUMMATION(X) / N


For large n, the distribution of sample sums Sn is close to normal distribution N(µ', σ') where:
	µ' = n x µ
	σ = n ** (1/2) * σ

 ]
 */
"""

# #########
# Imports
# #########

from typing import Tuple
import math

# #########
# Input
# #########

def get_input() -> Tuple[int, int, int, int]:
	"""Returns input for Central Limit Theorem I

	Returns:
		Tuple[int, int, int, int]: max_weight, boxes, mean, sd
	"""
	return 9800, 49, 205, 15


# #########
# Cumulative Distribution Function
# #########

def erf(x: int) -> float:
	"""Returns probability that random number in range [-x, x]

	Args:
		x (int): input of error function

	Returns:
		float: error for x
	
	NOTE:
		- Taken from: https://www.johndcook.com/blog/python_erf/
	"""
	constants = (
		1.061405429,
		-1.453152027,
		1.421413741,
		-0.284496736,
		0.254829592
	)
	p  =  0.3275911
	sign = 1 if x >= 0 else -1
	x = abs(x)
	t = 1 / (1 + p * x)
	y = 0

	for c in constants: y = (y + c) * t
	y = 1 - (y * math.exp(-x*x))

	return sign * y


def calc_cum_prob_norm_dist(x: int, mean: int, sd: int) -> float:
	"""Returns cumulative probability for a normal distribution from 0 to X.

	Args:
		x (int): Upper limit of cumulative probability
		mean (int): mean of sample
		sd (int): standard deviation of sample

	Returns:
		float: cumulative probability for [0, X].
	"""
	z = (x - mean) / (sd * 2 ** (1/2))
	return 1/2 * (1 + erf(z))


def print_to_scale(num: int) -> None:
	"""Prints number to 4 decimal places

	Args:
		num (int): Number to print
	"""
	print(f"{num :.4f}")


# #########
# Main
# #########

def main():
	"""
	NOTE:
	This is an interesting application of a normal distribution.

	Thus far, I have only used normal distribution assumptions when working with the mean. However, it makes sense
	for other statistics to follow the normal dist as well, e.g., the summation of a sample.

	As such, this solution uses a CDF to calculate the cumulative probability of 
	"""
	## Get Input
	max_weight, boxes, avg_weight, sd_weight = get_input()

	## Calculate sum & variance statistics to use
	normal_dist_sum = boxes * avg_weight
	normal_dist_sd = boxes ** (1/2) * sd_weight
	
	## Find Cumulative distribution
	cum_prob = calc_cum_prob_norm_dist(max_weight, normal_dist_sum, normal_dist_sd)

	print_to_scale(cum_prob)


if __name__ == "__main__":
	main()

