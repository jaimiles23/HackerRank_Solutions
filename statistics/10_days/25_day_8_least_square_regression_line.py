"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-26 16:47:26
 * @modify date 2020-09-26 17:04:43
 * @desc [
	Solution to: Day 8: Least Square Regression Line
		https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

This script contains 2 sections:	
	1. Notes
	2. Solution

##########
# Notes
##########

## Regression Line
If our data shows a linear relationship between X and Y, then the straight line which best describes the relationship is the regression line.
The regression line is given by Y = a + bX.

## Finding the Value of b
The value of b can be calculated using either of the following formulae:

1. b = 
	(n * Σ(xi*yi) - (Σxi) * (Σyi))  /  (n * Σ(xi**2) - (Σxi)**2)

2. b = 
	p * σY / σX
	- where p is the Pearson correlation coefficient.

## Finding the Value of a
	a = ȳ - b * x̄

## Sums of Squares
- Total Sum of Squares (SST) = Σ(yi - ȳ) ** 2
- Regression Sum of Squares (SSR) = Σ(ŷi - ȳ) ** 2
- Error Sum of Squares (SSE) = Σ(yi - ȳ) ** 2

NOTE:
	ŷ = predicted value
	ȳ = mean value
	yi = i-th value of y

If SSE is small, we can assume that our fit is good.

## Coefficient of Determination (R-squared)
	R**2 = SSR / SST = 1 - (SSE / SST)
R**2 multiplied by 100  gives the percent of variation attributed to the linear regression between Y and X.


## Example
Let's consider following data sets:
	x = [1,2,3,4,5]
	y = [2,1,4,3,5]

So,
	n = 5
	Σx = 15
	x̄ = 3
	Σy = 15
	ȳ = 3
	X**2 = Σ(x**2) = 55
	XY = Σ(xy) = 53

Compute b:
	b 
	=	(n * Σ(xi*yi) - (Σxi) * (Σyi))  /  (n * Σ(xi**2) - (Σxi)**2)
	=	(5 * 53 - 15 * 15) / (5 * 55 - 15 ** 2) 
		=	 40 / 50
			= 0.8

Compute a:
	a = ȳ - b * x̄
	= 3 - 0.8 * 3
		= 0.6

Regression equation: 
	ŷ = 0.6 + 0.8 * x





Now we can compute the values of  and :
And,
So, the regression line is .
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
def get_input() -> Tuple[list, list]:
	"""Returns tuple representing data points

	Returns:
		Tuple[list, list]: X and Y, respectively
	"""
	num_inputs = 5
	x, y = [], []
	for i in range(num_inputs):
		x_val, y_val = [float(val) for val in input().split()]
		x.append(x_val)
		y.append(y_val)

	return (x, y)


##########
# Mean
##########
def calc_mean(x: list) -> float:
	"""Returns mean of list

	Args:
		x (list): Input list

	Returns:
		float: mean of list
	"""
	return sum(x) / len(x)


##########
# Calculate b
##########

def calc_b(x: list, y: list) -> float:
	"""Returns b coefficient for x in simple linear regression

	Args:
		x (list): series 1
		y (list): series 2

	Returns:
		float: b coefficient for x
	"""
	n = len(x)
	xy = sum([x[i] * y[i] for i in range(len(x))])
	x_sq_sum = sum([val**2 for val in x])

	return (n * xy - sum(x) * sum(y)) / ( n * x_sq_sum - sum(x) ** 2)


##########
# Calculate A
##########

def calc_a(x: list, y: list, b: float) -> float:
	"""Returns `a` coefficient for regression equation.

	Args:
		x (list): predictor variable
		y (list): Outcome variable
		b (float): coefficient for predictor variable

	Returns:
		float: slope intercept
	"""
	return calc_mean(y) - b * calc_mean(x)


##########
# Predict
##########

def predict_val(a: float, b: float, x: int = 80) -> float:
	"""Predicts value for simple linear regression equation

	Args:
		a (float): Slope intercept constant
		b (float): Coefficient for x
		x (int): value of X

	Returns:
		float: predicted value of y
	"""
	return a + b * x


##########
# Print to scale
##########

def print_to_scale(num: float) -> None:
	"""Prints number to 3 decimal

	Args:
		num (float): Number to print
	"""
	print(f"{num :.3f}")


##########
# Main
##########

def main():
	x, y = get_input()

	b = calc_b(x, y)
	a = calc_a(x, y, b)

	prediction = predict_val(a, b)
	print_to_scale(prediction)


if __name__ == "__main__":
	main()


