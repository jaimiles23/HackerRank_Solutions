"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-25 15:33:54
 * @modify date 2020-09-25 16:48:18
 * @desc [
	Solution to: Day 5: Normal Distribution II
		https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem
 ]
 */
"""
##########
# Imports
##########

import math
from typing import Tuple


# #########
# Input
# #########

def get_input() -> Tuple[int, int, int, int]:
	"""Returns input for Normal Dist II.

	Returns:
		Tuple[int, int, int, int]: mean, sd, high_score, pass_threshold, respectively.
	"""
	return 70, 10, 80, 60
	mean, sd = [int(val) for val in input().split()]
	high_grade = int(input())
	pass_threshold = int(input())
	return mean, sd, high_grade, pass_threshold


# #########
# Error Function
# #########

def erf(x: int) -> float:
	"""Returns probability that random variable will be within range -x:x.

	Args:
		x (int): Random number to calculate error function

	Returns:
		float: Represents probability that random variable will be in range of x
	
	NOTE:
		- Implementation taken from [here](https://www.johndcook.com/blog/python_erf/)
	"""
	constants = (
		1.061405429,
		-1.453152027,
		1.421413741,
		-0.284496736,
		0.254829592,
	)
	p = 0.3275911
	sign = 1 if x >= 0 else -1
	x = abs(x)
	t = 1 / (1 + p * x)
	y = 0

	for c in constants: y = (y + c) * t
	y = 1 - (y * math.e ** (-x * x))
	return (y * sign)


# #########
# Cumulative Probability
# #########

def calc_norm_cum_prob(number: int, mean: int, sd: int) -> float:
	"""Returns cumulative probability of number from normal distribution

	Args:
		number (int): Number to calc cum prob for
		mean (int): Mean of the sample
		sd (int): Standard deviation of the sample

	Returns:
		float: Cumulative probability
	"""
	z = (number - mean) / (sd * 2 ** (1/2))
	cum_prob = 1/2 * ( 1 + erf(z))
	return cum_prob


# #########
# Format scale
# #########

def print_to_scale(num: float) -> float:
	"""Prints number to 3 decimal scale

	Args:
		num (float): Number to format

	Returns:
		float: Formatted number
	"""
	print(f'{num:.2f}')


# #########
# Main
# #########

def main():
	mean, sd, high_grade, pass_threshold = get_input()

	## % of students > high_grade
	high_test_grade = 1 - calc_norm_cum_prob(high_grade, mean, sd)

	## % of students failed test
	failed_test = calc_norm_cum_prob(pass_threshold, mean, sd)

	## % students passed test
	passed_test = 1 - failed_test
	output = [high_test_grade, passed_test, failed_test]
	output = [val * 100 for val in output]

	for o in output: print_to_scale(o)


if __name__ == "__main__":
	main()
