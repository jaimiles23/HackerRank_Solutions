"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-22 12:04:02
 * @modify date 2020-09-22 12:04:02
 * @desc [
	 Solution to: Day 5: Poisson Distribution I
		https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

This script contains 4 sections:
	1. Notes on the Poisson distribution
	2. Example problems of the Poisson distribution
	3. Math solution to Day 5: Poisson Distribution I
	4. Python solution


##########
# Notes
##########

##  Poisson Random Variables
We've already learned that we can break many problems down into terms of n, x, and p and use the following formula for binomial random variables:
	p(x) = combinations(n | x) * p ** x * q ** (n - x)


But what do we do when p(x) cannot be calculated using that formula? Enter the Poisson random variable.


## Poisson Experiment
A Poisson experiment is a statistical experiment that has the following properties:
	- binary outcome of experiment: Success (s) or failure (f)
	- average number of successes in specified region is known
	- Probability that success occurs is proportional to size of region
	- Probability that success occurs in extremely small region is virtually 0


## Poisson Distribution
A Poisson random variable is the number of successes that result from a Poisson experiment. 
The probability distribution of a Poisson random variable is called a Poisson distribution:
	P(k, λ) = (λ **k * e ** -λ) / k!

Where:
	- e = 2.71828
	- λ = average number of successes in region
	- k = actual number of successes in region
	- P(k, λ) is the Poisson probability to get exactly k successes when average success is λ.

##########
# Examples
##########

## Example 1
Acme Realty company sells an average of 2 homes per day. What is the probability that exactly 3 homes will be sold tomorrow?


Here, λ = 2 and k = 3, so 
	P(k, λ) = λ**k * e**-λ / k!
		= 2**3 * e**-2 / 3!
			= 8 * e**-2 / 6
				=  0.180

## Example 2
Suppose the average number of lions seen by tourists on a one-day safari is 5. 
What is the probability that tourists will see fewer than 4 lions on the next one-day safari?

- Summation of the Poisson distribution mass probability function from 1 to 3.
	P(0, 5) + P(1, 5) + P(2, 5) + P(3, 5)...
	P(1, 5) = 
		= P(k, λ) = λ**k * e**-λ / k!
			= 5**1 * e**-5 /1!
				= 5 * e**-5 / 1
					= 0.034
	P(2, 5) = 5**2 * e**-5 / 2
					= 0.084
	P(3, 5) = 5**3 * e**-5 / 6
					= 0.140
	P(0, 5) = 5 ** 0 * e**-5 / 0!
					= 0.007
	= 0.265

## Special Example
Consider some Poisson random variable, X. Let E[X] be the expectation of X. Find the value of E[X**2].

Let Var(X) be the variance of X. Recall that if a random variable has a Poisson distribution, then:

E[X] = λ
Var(X) = λ

The following is the property of expectation and variation for any random variable, X:
	Var(X) = E[X**2] - (E[x]) ** 2
	E[X**2] = Var(X) + E[x]) ** 2

Thus,
	E[X**2] = λ + λ ** 2


##########
# Math Solution
##########
A random variable, X, follows Poisson distribution with mean of 2.5. 
Find the probability with which the random variable X is equal to 5.

P(k, λ) = (λ **k * e ** -λ) / k!
P(5, 2.5) = 2.5 ** 5 * e ** -2.5 / k!
	= 0.067

 ]
 */
"""

##########
# Imports
##########

from typing import Tuple


##########
# Constants
##########

E = 2.71828


##########
# Input
##########
def get_input() -> Tuple[float, int]:
	"""Returns input for Day 5: Poisson Distribution I.

	Returns:
		Tuple[float, int]: X's mean and desired random variable value, respectively
	"""
	var_mean = float(input())
	desired_value = int(input())
	return (var_mean, desired_value)


##########
# Poisson Distribution
##########

def factorial(num: int) -> int:
	"""Returns factorial of num

	Args:
		num (int): Number to factorial

	Returns:
		int: Factorial result
	"""
	output = 1
	for i in range(num, 0, -1):
		output *= i
	return output


def calc_poisson_prob_mass(desired_value: int, val_mean: float) -> float:
	"""Returns mass probability for desired value in Poisson Distribution with val_mean. 

	Args:
		desired_value (int): Desired value of random variable, X
		val_mean (float): mean value of X

	Returns:
		float: Returns probability of desired value in Poisson Dist.
	"""
	return val_mean ** desired_value * E ** -val_mean / factorial(desired_value)


def format_scale(num: float) -> float:
	"""Returns number formatted to scale.

	Args:
		num (float): number to

	Returns:
		float: formatted number
	"""
	return f"{num:.3f}"


##########
# Main
##########

def main():
	var_mean, desired_value = get_input()

	prob = calc_poisson_prob_mass(desired_value, var_mean)
	print(format_scale(prob))


if __name__ == "__main__":
	main()

