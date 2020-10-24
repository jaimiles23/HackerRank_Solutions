# -*- coding: utf-8 -*-
"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-23 18:26:10
 * @modify date 2020-09-23 18:26:10
 * @desc [
	Solution to: Day 5: Normal Distribution I
		https://www.hackerrank.com/challenges/s10-normal-distribution-1/tutorial

This script contains 3 sections:
	1. Notes on normal distributions
	2. Python solution to the question

##########
# Notes
##########

## Normal Distribution
The probability density of normal distribution is:
	n(μ, σ) = 1 / (σ * 2π) ** 1/2 * e ** -(x-μ) ** 2 / 2σ**2

Here,
	μ is the mean (or expectation) of the distribution. It is also equal to median and mode of the distribution.
	σ**2 is the variance.
	σ is the standard deviation.

## Standard Normal Distribution
If μ = 0 and σ = 1, then the normal distribution is known as standard normal distribution:
	σ(x) = e ** - x**2/2 / (π) ** 1/2

Every normal distribution can be represented as standard normal distribution:
	n(μ, σ**2) = 1/σ * Standard Normal Dist * ((x - μ)/σ)


## Cumulative Probability
Consider a real-valued random variable, X. The cumulative distribution function of X (or just the distribution function of X) 
evaluated at x is the probability that X will take a value less than or equal to x:

	Fx(x) = P(X <= x)
Also,
	P(a <= X <= b) = P(a < X < b) = Fx(b) - Fx(a)

The cumulative distribution function for a function with normal distribution is:
	cumdist(x) = 1/2(1 + erf(x - μ) / σ * 2**1/2)

Where erf is the error function:
	erf(z) = 2/π, summation 0 to z, e ** -x** * dx
]
*/
"""

# #########
# Imports
# #########

from typing import Tuple


# #########
# Constants
# #########

import math


# #########
# Input
# #########

def get_input() -> Tuple[int, int, float, ]:
	"""Returns input for Day 5: Normal Distribution I

	Returns:
		Tuple[int, int, float, int]: Represents: mean, sd, less than value, and interval
	"""
	return (20, 2, 19.5, 20, 22)

	mean, sd = (int(x) for x in input().split())
	less_than = float(input())
	interval_1, interval_2 = (int(x) for x in input().split())
	return mean, sd, less_than, interval_1, interval_2


# #########
# Cumulative Probability function
# #########

def custom_erf(z: int) -> float:
	"""Returns error from error function for normal distribution

	Args:
		z (int): error function value

	Returns:
		float: error amount
	
	NOTE:
		- math module has an inbuilt erf function
		- dt represents an infinitely small value from a Maclaurin series
		- formula taken from: https://www.johndcook.com/blog/python_erf/
	"""
	## Vars
	constants = (
		1.061405429,
		-1.453152027,
		1.421413741,
		-0.284496736,
		0.254829592,
	)
	p = 0.3275911
	sign = 1 if z >= 0 else -1
	z = abs(z)
	t = 1 / ( 1 + p * z)

	## Calc
	y = 0
	for c in constants: y = (y + c) * t
	y = 1 - (y * math.e ** (-z * z))

	return y * sign


def calc_cum_distr(x: int, mean: float,	sd: float) -> float:
	"""returns cumulative probability for val in normal distribution.

	Args:
		x (int): value to find cum probability for

	Returns:
		float: cumulative probability of x
	"""
	z = (x - mean) / (sd * 2 ** (1/2))
	return 1/2 * (1 + custom_erf(z))


def format_scale(num: float) -> float:
	"""Formats number to scale

	Args:
		num (float): number

	Returns:
		float: formatted number
	"""
	return f'{num :.3f}'


# #########
# Main
# #########

def main():
	"""Runs script
	"""
	## Input
	mean, sd, less_than, interval_1, interval_2 = get_input()

	## Cum prob for less than
	cum_prob_less_than = calc_cum_distr(less_than, mean, sd)
	print( format_scale(cum_prob_less_than))

	## Interval cum prob
	int1_cum_prob = calc_cum_distr(interval_1, mean, sd)
	int2_cum_prob = calc_cum_distr(interval_2, mean, sd)
	interval_cum_prob = int2_cum_prob - int1_cum_prob
	print( format_scale(interval_cum_prob))


if __name__ == "__main__":
	main()

	
