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




