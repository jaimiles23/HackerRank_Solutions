"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-18 09:55:46
 * @modify date 2020-09-18 09:55:46
 * @desc [
	Solution to: Day 4: Binomial Distribution I
		https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

This script contains 2 sections:
	1. Notes on binominal distributions
	2. Example problem
	3. Solution to Day 4: Binomial Distribution I
 ]
 */
"""

##########
# Imports
##########

from typing import Tuple


##########
# Notes on binomial distributions
##########
"""
## Random Variable
A random variable, 	X, is the real-valued function X: S -> R in which there is an event for each interval I where I <=R. 
You can think of it as the set of probabilities for the possible outcomes of a sample space. 
For example, if you consider the possible sums for the values rolled by 2 four-sided dice:
	X = {2, 3, 4, 5, 6, 7, 8}
	P(X = 2) = P({ (1, 1)}) = 1/16
	P(X = 3) = P({ (1, 2), (2, 1)}) = 2/16
	P(X = 4) = P({ (1, 3), (2, 2), (3, 1)}) = 3/16
	P(X = 5) = P({ (1, 4), (2, 3), (3, 2), (4, 1)}) = 4/16
	P(X = 6) = P({ (2, 4), (3, 3), (4, 2)}) = 3/16
	P(X = 7) = P({ (3, 4), (4, 3)}) = 2/16
	P(X = 8) = P({ (4, 4)}) = 1/16


## Binomial Experiment
A binomial experiment (or Bernoulli trial) is a statistical experiment that has the following properties:
	- The experiment consists of n repeated trials.
	- The trials are independent.
	- The outcome of each trial is either success (s) or failure (f).


## Bernoulli Random Variable and Distribution
The sample space of a binomial experiment only contains two points: s and f. 
We define a Bernoulli random variable to be the random variable defined by X(s) = 1 and X(f) = 0. 
If we consider the probability of success to be p and the probability of failure to be q (where q = 1-p), 
then the probability mass function (PMF) of X is:
	P(x):
		= 1-p=q, if x = 0
		= p if x = 1
		= 0 otherwise


This is also expressed as:
	f(x) = p**x(1 - p) ** (1-x), for x {0, 1}

## Binomial Distribution
We define a binomial process to be a binomial experiment meeting the following conditions:

	- The number of successes is x.
	- The total number of trials is n.
	- The probability of success of 1 trial is p.
	- The probability of failure of 1 trial q, where q = 1 - p.
	- b(x, n, p) is the binomial probability, meaning the probability of having exactly x successes out of n trials.

The binomial random variable is the number of successes, x, out of n trials.

The binomial distribution is the probability distribution for the binomial random variable, given by the following probability mass function:
	b(x, n, p) = (n | x) * p**x * q ** (n-x)

Note: Recall that (n|x) is notation for combinations, and solved:
	nCr:
		= nPr | !r 
			= n! / (r! * (n-r)!)


## Cumulative Probability
We consider the distribution function for some real-valued random variable, X, to be Fx(X)  = P(x <= X). 
Because this is a non-decreasing function that accumulates all the probabilities for the values of x up to (and including) X, 
we call it the cumulative distribution function (CDF) of X. 

As the CDF expresses a cumulative range of values, we can use the following formula to find the cumulative probabilities for all x [a, b]:
	P(a < X <= b) = Fx(b) - Fx(a)

This formula takes a summation of the binomial probability mass function
"""

##########
# Example Problems
##########
"""
NOTE: Solutions to the example problems are printed in the main script below*

A fair coin is tossed n times. Find the following probabilities:

- Getting 5 heads.
- Getting at least 5 heads.
- Getting at most 5 heads.

## 1. Getting 5 heads.
To calculate the probability distribution of a binomial distribution, use the binominal probability mass function:
	b(x, n, p) = (n | x) * p**x * q ** (n-x)

b(5, 10, 0.5) 
	= (10 | 5) ** 0.5**5 * 0.5**(1-0.5)
		= (10! / (5! * (10 - 5)!) ** 0.5**5 * 0.5**5
			= 0.24609

## Getting at least 5 heads:
	= Summation from 1, 5 of b(x, n, p).

## Getting 5+ heads
	= Summation from 5, 10 of b(x, n, p)
"""

##########
# Example problem code
##########
""" Functions to calculate Binomial Mass Probability Functions
"""

def factorial(num: int) -> float:
	"""Returns factorial for num

	Args:
		num (int): Number to get factorial

	Returns:
		float: Factorial of num
	"""
	if num == 0:
		return 1

	output = num
	for i in range(num-1, 0, -1):
		output *= i
	return output


def calc_bin_mass_prob_func(x: int, n: int, p: float) -> float:
	"""Returns the probability of X/N trials in binomial probability distribution defined by p.

	Args:
		x (int): successes
		n (int): total trials
		p (float): probability of success

	Returns:
		float: mass probability to return x successes
	"""
	q = 1 - p

	combinations = factorial(n) / (factorial(x) * factorial(n - x))
	mass_prob = combinations * p ** x * q ** (n-x)
	return mass_prob


def calc_bin_cum_dist_func(r: int, x: int, n: int, p: float) -> float:
	"""Returns the cumulative distribution of range r:x (inclusive) trials out of n.

	Args:
		r (int): lower limit of dist
		x (int): upper limit of dist
		n (int): total number of trials
		p (float): probability of success

	Returns:
		float: cumulative distribution of range r - x
	"""
	cum_dist = 0
	for i in range(r, x + 1):
		mass_dist = calc_bin_mass_prob_func(i, n, p)
		cum_dist += mass_dist
	return cum_dist


##########
# Binomial Distribution Problem
##########
"""
The ratio of boys to girls for babies born in Russia is 1.09: 1. 
If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

Input Format:
A single line containing the following values:
1.09 1
"""
##### Imports
from typing import Tuple


##### Input
def get_input() -> Tuple[float, int]:
	"""Returns ipnut for binomial distribution problem i

	Returns:
		Tuple[float, int]: Represents respective probabilities of girl and boy babies.
	"""
	girl_prob, boy_prob = [x for x in input().split()]
	return (float(girl_prob), int(boy_prob))


##### Get p
def get_probability_p(girl_prob: float, boy_prob: int, desired_sex: str) -> float:
	"""Returns probability of successful trial.

	Args:
		girl_prob (float): P(girl)
		boy_prob (int): P(boy)
		desired_sex (str): calc p for sex

	Returns:
		float: [description]
	"""
	if desired_sex == 'm':
		return boy_prob / (girl_prob + boy_prob)
	return girl_prob / (girl_prob + boy_prob)


def factorial(num: int) -> float:
	"""Returns factorial for num

	Args:
		num (int): Number to get factorial

	Returns:
		float: Factorial of num
	"""
	if num == 0:
		return 1

	output = num
	for i in range(num-1, 0, -1):
		output *= i
	return output


def get_bin_mass_dist(x, n, p) -> float:
	"""Returns binomial mass distribution of p(x, n, p).

	Args:
		x ([type]): Success trials
		n ([type]): Total Trials
		p ([type]): P(X)

	Returns:
		float: probability mass distribution
	"""

	combinations = factorial(n) / (factorial(x) * factorial(n - x))
	bin_mass = combinations * p ** x * (1 - p) ** (n - x)
	return bin_mass


def get_cum_prob_bin_dist(r: int, x: int, n: int, p: float) -> float:
	"""Returns cumulative prob of binary distribution with inclusive limits [r:x].

	Args:
		r (int): lower limit of dist
		x (int): upper limit of dist
		n (int): total trial
		p (float): probability of x

	Returns:
		float: cumulative probability of binary distribution
	"""
	cum_prob = 0
	for i in range(r, x + 1):
		bin_mass = get_bin_mass_dist(i, n, p)
		cum_prob += bin_mass
	return cum_prob


def solution() -> None:
	"""Prints solution to Day 4: Binomial Distribution i.
	"""
	## Constants
	N = 6
	R = 3
	X = 6
	DESIRED_SEX = 'b'

	## funcs
	girl_prob, boy_prob = get_input()
	p = get_probability_p(girl_prob, boy_prob, DESIRED_SEX)
	cum_prob = get_cum_prob_bin_dist(R, X, N, p)
	print("{0:.3f}".format(cum_prob))


##########
# Main
##########

def main():
	"""Prints solutions to:
		- Example problems 1, 2, & 3.
		- Day 4: Binomial Distribution i problem.
	"""
	print("\nExample 1")
	x, n, p = 5, 10, 0.5
	print(calc_bin_mass_prob_func(x, n, p))

	print("\nExample 2")
	r, x, n, p = 0, 5, 10, 0.5
	print( calc_bin_cum_dist_func(r, x, n, p))

	print("\nExample 3")
	r, x, n, p = 5, 10, 10, 0.5
	print( calc_bin_cum_dist_func(r, x, n, p))

	print("\nSolution Problem")
	solution()



if __name__ == "__main__":
	main()
