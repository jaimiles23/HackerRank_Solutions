"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-26 12:41:10
 * @modify date 2020-09-26 12:59:26
 * @desc [
	Solution to: Day 7: Spearman's Rank Correlation Coefficient
		https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

This script contains 3 sections:
	1. Notes on Spearman's Rank Correlation Coefficient
	2. Solution with Standard Spearman Rank Correlation Coefficient Solution
	3. Solution with Spearman Rank Special Case for Unique Values


##########
# Notes
##########

## Spearman's Rank Correlation Coefficient

We have two random variables, X and Y:
	X = (x1, x2, x3, ... xn)
	Y = (y1, y2, y2, ... yn)

If Rank_x and Rank_y denote the respective ranks of each data point, then the Spearman's rank correlation coefficient, Rs, 
is the Pearson correlation coefficient of Rank_x and Rank_y.

## Example
	X = {0.2, 1.3, 0.2, 1.1, 1.4, 1.5}
	Y = {1.9, 2.2, 3.1, 1.2, 2.2, 2.2}

Rank_x correlating to X:
	Rank_x = [1, 3, 1, 2, 4, 5]
Rank_y correlating to Y:
	Rank_y = [2, 3, 4, 1, 3, 3]

Rs = the Pearson correlation coefficient of rank_x and rank_y, or 0.158114

## Special Case: X and Y don't contain duplicates
rs = 1 - 6 summation(di**2) / (n * (n**2 - 1))

[Proof](https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/tutorial)]
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
	"""Returns input for Spearman's rank correlation coefficient.

	Returns:
		Tuple[int, float, float]: number of items, x, y
	"""
	num_items = int(input())
	x = [float(val) for val in input().split()]
	y = [float(val) for val in input().split()]
	return num_items, x, y


##########
# Print
##########

def print_to_scale(num: int) -> None:
	"""Prints number formatted to 3 decimal scale.

	Args:
		num (int): Number to print to scale
	"""
	print(f"{num :.3f}")


##########
# Spearman's Rank
##########

def get_ranks(x: list) -> list:
	"""Returns corresponding ranks of x list.

	Args:
		x (list): List to rank

	Returns:
		list: Rankings of x
	"""
	x_sorted = sorted(x)

	## Get rank of each val
	val_ranks = dict()
	for i in range(len(x_sorted)):
		val_ranks[x_sorted[i]] = (i + 1)

	## Create ranking
	x_ranks = []
	for val in x:
		x_ranks.append( val_ranks[val])	
	return x_ranks


def calc_mean(x: list) -> float:
	"""Returns mean of list

	Args:
		x (list): list to mean

	Returns:
		float: mean of x
	"""
	return sum(x) / len(x)


def calc_sd(x: list) -> float:
	"""Returns standard deviation of list, x.

	Args:
		x (list): List to get sd

	Returns:
		float: standard deviation of x
	"""
	x_mean = calc_mean(x)
	sd_num = 0
	for val in x:
		sd_num += (val - x_mean) ** 2
	return (sd_num / len(x)) ** (1/2)


def calc_cov(num_items: int, x: list, y: list) -> float:
	"""Calculates covariance for (x, y).

	Args:
		num_items (int): length of x, y
		x (list): series 1
		y (list): series 2

	Returns:
		float: covariance between x and y.
	"""
	mean_x, mean_y = calc_mean(x), calc_mean(y)

	numerator = 0
	for i in range(num_items):
		numerator += (x[i] - mean_x) * (y[i] - calc_mean(y))
	
	return numerator / num_items


def calc_spearmans_coef(num_items: int, x: list, y: list) -> float:
	"""Returns spearman's coefficient for x,y

	Args:
		num_items (int): length of both lists
		x (list): series 1
		y (list): series 2

	Returns:
		float: Spearman's coefficient for (x, y)
	"""
	assert len(x) == len(y)
	rank_x, rank_y = get_ranks(x), get_ranks(y)

	cov = calc_cov(num_items, rank_x, rank_y)
	sd_x, sd_y = calc_sd(x), calc_sd(y)

	return cov / (sd_x * sd_y)




	
