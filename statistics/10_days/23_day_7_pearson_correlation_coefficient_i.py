"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-26 12:13:06
 * @modify date 2020-09-26 12:13:06
 * @desc [
	Solution to: Day 7: Pearson Correlation Coefficient I
		https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem
	
This script contains:
	1. Notes on Covariance
	2. Solution to Pearson Correlation Coefficient I

##########
# Notes
##########

## Covariance
This is a measure of how two random variables change together, or the strength of their correlation.


Consider two random variables, X and Y, each with n values (i.e., x1, x2, x3, ... xn  and y1, y2, y3, ... yn ). 
The covariance of X and Y can be found using the following formula:

	cov(X, Y) = (1/n) * Σ(i=1,n)[(x - x̄) * (y - ȳ)]

## Pearson Correlation Coefficient
The Pearson correlation coefficient, ρxy, is given by:

	ρ(xy) = cov(X, Y) / σx * σy

You may also see ρ(xy) written as r(xy).
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
def get_input() -> Tuple[int, list, list]:
	"""Returns input for Pearson Correlation Coefficient I

	Returns:
		Tuple[int, list, list]: num items, X, Y
	"""
	num_items = int(input())
	x = [float(val) for val in input().split()]
	y = [float(val) for val in input().split()]
	return num_items, x, y


##########
# Covariance
##########

def calc_mean(x: list) -> float:
	"""Returns mean of list

	Args:
		x (list): List to calculate mean

	Returns:
		float: Mean of x
	"""
	return sum(x) / len(x)


def calc_sd(x: list) -> float:
	"""Returns standard deviation of list.

	Args:
		x (list): List to calculate sd

	Returns:
		float: Sd of list
	"""
	x_mean = calc_mean(x)
	
	sd_num = 0
	for item in x:
		sd_num += (item - x_mean) ** 2

	return (sd_num / len(x)) ** (1/2)


def calc_cov(num_items: int, x: list, y: list) -> float:
	"""Returns covariance for x and y

	Args:
		num_items (int): length of x and y
		x (list): series 1
		y (list): series 2

	Returns:
		float: covariance between x and y
	"""
	assert len(x) == len(y)
	mean_x, mean_y = calc_mean(x), calc_mean(y)

	cov_total = 0
	for i in range(num_items):
		cov_total += (x[i] - mean_x) * (y[i] - mean_y)
	return cov_total / num_items


def calc_pearson_coef(num_items: int, x: list, y: list) -> float:
	"""Returns pearson's coefficient between two lists."""
	cov = calc_cov(num_items, x, y)
	sd_x, sd_y = calc_sd(x), calc_sd(y)

	return cov / (sd_x * sd_y)


def print_to_scale(num: int) -> None:
	"""Prints number to 3 decimal places.

	Args:
		num (int): Number to print
	"""
	print(f"{num :.3f}")


##########
# Main
##########
def main():
	num_items, x, y = get_input()
	pearson_coef = calc_pearson_coef(num_items, x, y)
	print_to_scale(pearson_coef)


if __name__ == "__main__":
	main()
