"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-11 17:23:28
 * @modify date 2020-09-11 17:31:06
 * @desc [
	Solution to: Day 0: Weighted Mean
		https://www.hackerrank.com/challenges/s10-weighted-mean

## Wiki definition
The weighted arithmetic mean is similar to an ordinary arithmetic mean (the most common type of average), 
except that instead of each of the data points contributing equally to the final average, some data points contribute more than others. 
The notion of weighted mean plays a role in descriptive statistics and also occurs in a more general form in several other areas of mathematics.

If all the weights are equal, then the weighted mean is the same as the arithmetic mean. 

## NOTE:
	- Output scaled to 1 decimal place

 ]
 */
"""

# #########
# Imports
# #########

from typing import List, Tuple, Union

# #########
# Constants
# #########

SCALE = 1	# number of decimals


# #########
# Input
# #########

def get_input() -> Tuple[int, list, list]:
	"""Returns 3 variabless:
		n: int, length of list
		nums: list, numbers to calculate
		weights: list, weight of numbers.
		"""
	n = int(input())
	nums = [int(val) for val in input().split()]
	weights = [int(val) for val in input().split()]
	return (n, nums, weights)


# #########
# Weighted Mean
# #########

def calc_weighted_mean(n: int, nums: List[int], weights: List[int]) -> float:
	"""Returns weighted mean from list of nums and weights with length n."""
	assert (len(nums) == n) and (len(weights) == n)

	weighted_total = 0
	for i in range(n):
		weighted_total += nums[i] * weights[i]
	
	return format_scale( weighted_total / sum(weights))


# #########
# Format scale
# #########

def format_scale(num: Union[int, float]) -> Union[int, float]:
	if isinstance(num, int):
		return num
	
	return round(num, 1)


# #########
# Main
# #########

def main():
	n, nums, weights = get_input()
	print( calc_weighted_mean(n, nums, weights))


if __name__ == "__main__":
	main()
