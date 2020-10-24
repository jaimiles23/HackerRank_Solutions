"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-22 13:39:33
 * @modify date 2020-09-22 13:39:33
 * @desc [
	Solution to: Day 5: Poisson Distribution II
		https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

########## NOTE
From the tutorial, we can find the Expectation of X by considering the following:

Consider some Poisson random variable, X. Let E[x] be the expectation of X. Find the value of E[X**2].

Let Var(X) be the variance of X. Recall that if a random variable has a Poisson distribution, then:
	E[X] =  λ
	Var(X) =  λ

Now, we'll use the following property of expectation and variance for any random variable, X:
So, for any random variable X having a Poisson distribution, the above result can be rewritten as:

	Var(X) = E[X**2] - E[X]**2
	E[X**2] = Var(X) + E[X]**2
Thus, for any random variable, X, having a Poisson distribution, the result can be written as:
	E[X**2] =  λ +  λ**2 

This formula means that the expectation of X**2 is the mean squared + the variance
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

def get_input() -> Tuple[float, float]:
	"""Returns input for Day 5: Poisson Distribution II.

	Returns:
		Tuple[float, float]: Represents mean values for machines A and B respectively.
	"""
	a_cost, b_cost = [float(val) for val in input().split()]
	return a_cost, b_cost


##########
# Calculate Expected Costs
##########

def calc_expected_operating_costs(poisson_mean: float, coefficient: int, constant: int) -> float:
	"""Return cost of operating machine with arguments

	Args:
		poisson_mean (float): Poisson random variable mean
		coefficient (int): Coefficient to include in linear cost calculations
		constant (int): Constant to add

	Returns:
		float: Represents daily cost of operating machine
	"""
	mean_squared_cost = calc_expected_squared_cost(poisson_mean)

	return coefficient * mean_squared_cost + constant


def calc_expected_squared_cost(poisson_mean: float) -> float:
	"""Returns expected squared cost

	Args:
		poisson_mean (float): Poisson random variable mean

	Returns:
		float: Expected cost of mean squared
	"""
	return poisson_mean + poisson_mean ** 2


def format_scale(num: float) -> float:
	"""Returns number formatted to scale

	Args:
		num (float): Number to format

	Returns:
		float: formatted number
	"""
	return f"{num :.3f}"


##########
# Main
##########
def main():
	a_mean, b_mean = get_input()

	a_constant, a_coeff = 160, 40
	b_constant, b_coeff = 128, 40

	a_cost = calc_expected_operating_costs(a_mean, a_coeff, a_constant)
	b_cost = calc_expected_operating_costs(b_mean, b_coeff, b_constant)

	print(format_scale(a_cost))
	print(format_scale(b_cost))


if __name__ == "__main__":
	main()
