"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-12 10:22:28
 * @modify date 2020-09-12 10:22:28
 * @desc [Solution to: Day 1: Quartiles
		https://www.hackerrank.com/challenges/s10-quartiles]
	
## Wiki definition:
A quartile is a type of quantile which divides the number of data points into four more or less equal parts, or quarters. 
The first quartile (Q1) is defined as the middle number between the smallest number and the median of the data set. 
It is also known as the lower quartile or the 25th empirical quartile and it marks where 25% of the data is below or to the left of it 
(if data is ordered on a timeline from smallest to largest). 
The second quartile (Q2) is the median of a data set and 50% of the data lies below this point. 
The third quartile (Q3) is the middle value between the median and the highest value of the data set.
It is also known as the upper quartile or the 75th empirical quartile and 75% of the data lies below this point.[1]

Due to the fact that the data needs to be ordered from smallest to largest to compute quartiles, quartiles are a form of Order statistic.


## Process:
As an ordered statistic, we can derive Q1, Q2, and Q3 via finding the the median of different sections of data.
	Q1: min : Q2
	Q2: min : max
	Q3: Q2 : max

## Implementation
To implement, I will create a median function and find Q2 (the median) of the data set. 
Then, I will calculate Q1 and Q3 refernecing Q2.
*/
"""

##########
# Imports
##########

import typing


##########
#
##########








