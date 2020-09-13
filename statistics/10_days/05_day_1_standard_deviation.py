"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-12 11:29:49
 * @modify date 2020-09-12 20:34:51
 * @desc [Solution to: Day 1: Standard Deviation
		https://www.hackerrank.com/challenges/s10-standard-deviation/problem]

## Wiki Definition
In statistics, the standard deviation is a measure of the amount of variation or dispersion of a set of values.
A low standard deviation indicates that the values tend to be close to the mean (also called the expected value) of the set, 
while a high standard deviation indicates that the values are spread out over a wider range.

## Formula
sd = (Summation{(xi - mean) ** 2)}) ** 1/2 / n

## NOTE:
	- Scale of 1 decimal

 */
"""

##########
# Imports
##########

from typing import List, Tuple


##########
# Input
##########

def get_inputs() -> Tuple[int, list]:
	"""Return tuple of inputs:
	- n: int, number of elements in array.
	- nums: list, data elements
	"""
	n = int(input())
	nums = [int(val) for val in input().split()]

	return (n, nums)


##########
# Standard Deviation
##########

def calc_stdev(n: int, nums: List[int]) -> float:
	"""Returns standard deviation from nums."""
	tot_squared_dist_from_mean = 0
	avg = sum(nums) / n

	for num in nums:
		dist_from_mean = (num - avg) ** 2
		tot_squared_dist_from_mean += dist_from_mean
	
	variance = tot_squared_dist_from_mean / n
	return variance ** (1/2)


##########
# Format scale
##########

def format_scale(num: float) -> float:
	"""Formats number to 1 decimal place."""
	return '{0:.1f}'.format(num)


##########
# Main
##########

def main():
	## Input
	n, nums = get_inputs()

	## Calc sd
	sd = calc_stdev(n, nums)
	
	## print
	print(format_scale(sd))


if __name__ == "__main__":
	main()