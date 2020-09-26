"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-25 18:22:09
 * @modify date 2020-09-25 18:22:09
 * @desc [
	Solution to: Day 6: The Central Limit Theorem II
		https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

NOTE: This solution uses a characteristic of a normal distribution that ANY summary statistic will follow a normal dist.

Thus, this script uses a CDF (Cumulative Density Function) to calculate the cumulative probability of return <= 250
 ]
 */
"""

##########
# Imports
##########

import math
from typing import Tuple


##########
# Input
##########

def get_input() -> Tuple[int, int, int, int]:
	"""Returns input for Central Limit Theorem II

	Returns:
		Tuple[int, int, int, int]: num_tickets, students, mean, sd, respectivel
	"""
	return 250, 100, 2.4, 2


##########
# CDF
##########

def erf(x: int) -> float:
	"""Returns probability that random var in range defined by x

	Args:
		x (int): number to calculate err

	Returns:
		float: probability that random var falls in range
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


def calc_cum_prob_norm_dist(num: int, mean: int, sd: int) -> float:
	"""Returns cumulative probability `num` in a normal distribution

	Args:
		num (int): number to calculate cumulative probability to
		mean (int): sample mean
		sd (int): sample std

	Returns:
		float: cum probability up to num
	"""
	z = (num - mean) / (sd * 2 ** (1/2))
	return 1/2 * (1 + erf(z))


def print_to_scale(num: int) -> None:
	"""Prints number to 4 decimal places

	Args:
		num (int): Number to print
	"""
	print(f"{num :.4f}")


###########
# Main
###########

def main():

	## Input
	tickets, students, mean_tickets, sd_tickets = get_input()

	## Summary stats to calculate cum prob
	sum_norm_dist = students * mean_tickets
	sd_norm_dist = students ** (1/2) * sd_tickets

	## Find cumulative dist
	cum_prob = calc_cum_prob_norm_dist(tickets, sum_norm_dist, sd_norm_dist)

	print_to_scale(cum_prob)


if __name__ == "__main__":
	main()