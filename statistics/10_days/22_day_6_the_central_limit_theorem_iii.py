# -*- coding: utf-8 -*-
"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-26 10:11:33
 * @modify date 2020-09-26 11:40:25
 * @desc [
	Solution to: Day 6: The Central Limit Theorem III
		https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

This solution utilizes the formula to determine a z-score:
	z = (x -  μ) / σ

Because the problem gives us the z-score and asks us to find the bounds, we can solve the formula for x:
	x = (z * σ) + μ

The true values are: mean_sample = mean_population, and sd_sample = sd_population / sqrt(n)
NOTE: 
	When extrapolating sample statistics to population statistics, the following are derived from the Central Limit Theorem:
		1. mean_sample = mean_population
		2. standard error (population) = sd_sample / sqrt(n)
			This is because as the sample increases, means cluster more closely around the mean
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

def get_input() -> Tuple[int, int, int, float, float]:
	"""Returns input for Day 6: Central Limit Theorem III.

	Returns:
		Tuple[int, int, int, float, float]: num_students, mean, sd, distribution percent, z-score
	"""
	return 100, 500, 80, 0.95, 1.96


# #########
# Calculate val from z-score
# #########

def calc_std_err(sd: int, n: int) -> float:
	"""Returns standard error of population

	Args:
		sd (int): Standard deviation
		n (int): Sample

	Returns:
		float: Standard error
	"""
	return sd / (n ** (1/2))


def calc_val_from_zscore(z_score: float, mean: int, sd: int) -> float:
	"""Returns value associated with the z-score from sample mean & sd.

	Args:
		z_score (float): z-score
		mean (int): sample mean
		sd (int): sample sd

	Returns:
		float: value assocaited with z-score given sample mean & sd
	"""
	return z_score * sd + mean


def print_to_scale(num: int) -> None:
	"""Prints number to 2 decimal point scale

	Args:
		num (int): Number to print
	"""
	print(f"{num :.2f}")


##########
# Main
##########
def main():
	num_students, mean, sd, dist_percent, z_score = get_input()
	std_err = calc_std_err(sd, num_students)

	## Bottom bound of dist_percent
	a = calc_val_from_zscore(-z_score, mean, std_err)
	## Top bound of dist_percent
	b = calc_val_from_zscore(z_score, mean, std_err)

	## Print
	print_to_scale(a)
	print_to_scale(b)


if __name__ == "__main__":
	main()
