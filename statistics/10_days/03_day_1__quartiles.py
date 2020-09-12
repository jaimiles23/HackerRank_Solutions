"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-12 10:22:28
 * @modify date 2020-09-12 10:45:24
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
As an ordered statistic, we can derive Q1, Q2, and Q3 via finding the the median of different sets of data.
Data Sets for:
	Q1: min - Q2
	Q2: min - max
	Q3: Q2 - max

## Implementation
To implement, I will create a median function and find Q2 (the median) of the data set. 
Then, I will find the data set for Q1 and Q3, and calculate the median for those data sets as well.

## Method NOTE:
- There is no universal agreement on selecting quartile values for the discrete distributions. 
- This solution does not include the median in the data used to calculate Q1 and Q3.

*/
"""

##########
# Imports
##########

from typing import List, Tuple, Union


##########
# Inputs
##########

def get_input() -> Tuple[int, List[int]]:
	"""Returns input for n: number of integers and nums: list of integers."""
	n = int(input())
	nums = sorted([int(val) for val in input().split()])
	assert n == len(nums)
	return (n, nums)


##########
# Median method
##########

def calc_median(nums: list) -> Union[int, float]:
	"""Returns the median value from a list of nums with length n."""

	mid, remainder = divmod(len(nums), 2)
	if remainder:
		return nums[mid]
	
	median = sum(nums[mid-1: mid+1]) / 2
	return format_int(median)


def get_q_data(nums: list, quartile: str) -> List[int]:
	"""Returns list of data to calculate relevant quantile (Q1, Q3).

	quartile argument used to determine data boundary index for Q1 or Q3.
	"""	
	assert quartile in (1, 3)
	n = len(nums)
	bound = 0 if quartile == 1 else n	# calculate data index boundary

	mid, remainder = divmod(n, 2)
	if remainder:
		mid = mid + 1 if (quartile == 3) else mid	# exclude middle data point in odd number solutions

	b1, b2 = sorted([bound, mid])
	return nums[b1:b2]


##########
# Format
##########

def format_int(num: Union[float, int]) -> Union[float, int]:
	"""Formats decimal integer to integer else returns float"""
	if num.is_integer():
		return int(num)
	return num


##########
# Main
##########

def main():
	## Input
	n, nums = get_input()

	## Q2
	q2 = calc_median(nums)

	## Get Q1&3 data
	q1_data = get_q_data(nums, quartile=1)
	q3_data = get_q_data(nums, quartile=3)

	## Calc Q1&3
	q1 = calc_median(q1_data)
	q3 = calc_median(q3_data)

	## Print
	quantiles = [q1, q2, q3]
	print(*quantiles, sep = '\n')


if __name__ == "__main__":
	main()

