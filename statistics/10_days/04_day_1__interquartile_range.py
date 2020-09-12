"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-12 15:12:07
 * @modify date 2020-09-12 15:12:07
 * @desc [
	Solution to: Day 1: Interquartile Range
		https://www.hackerrank.com/challenges/s10-interquartile-range/problem

## Wiki definition
In descriptive statistics, the interquartile range (IQR), is a measure of statistical dispersion,
being equal to the difference between 75th and 25th percentiles, or between upper and lower quartiles,[1][2] IQR = Q3 −  Q1. 

It is a trimmed estimator, defined as the 25% trimmed range, and is a commonly used robust measure of scale.
 ]
 */
"""

##########
# Imports
##########

from typing import List, Tuple, Union


##########
# Input
##########

def get_input() -> Tuple[int, List[int], List[int]]:
	"""Returns a tuple of problem input.
	n: int, number of elements
	x: list, list of integers
	f: list, list of integers, index corresponds to frequency of the index of x elements.
	"""
	n = int(input())
	x = [int(val) for val in input().split()]
	f = [int(val) for val in input().split()]
	return (n, x, f)


##########
# Main
##########

def main():
	pass


if __name__ == "__main__":
	main()

