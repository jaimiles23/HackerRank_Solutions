"""
 /**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-12 15:12:07
 * @modify date 2020-09-12 17:59:06
 * @desc [
	Solution to: Day 1: Interquartile Range
		https://www.hackerrank.com/challenges/s10-interquartile-range/problem

## Wiki definition
In descriptive statistics, the interquartile range (IQR), is a measure of statistical dispersion,
being equal to the difference between 75th and 25th percentiles, or between upper and lower quartiles,[1][2] IQR = Q3 −  Q1. 

It is a trimmed estimator, defined as the 25% trimmed range, and is a commonly used robust measure of scale.

## Notes:
- Do not include median in upper OR lower data sets.

## Process:
- Create dictionary of values and frequencies before sorting values. 
	Using a dictionary and sorting the keys has a better practical time complexity than sorting a complete list of values.
 ]
 */
"""

##########
# Imports
##########

from typing import Dict, List, Tuple, Union


##########
# Constants
##########
SCALE = 1


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
# Create list of elements
##########

def get_master_list(nums: List[int], freq: List[int]) -> List[int]:
	"""Returns list of ints with appropriate frequencies.
	
	2 auxiliary functions:
	- Create_val_freq_dict
	- create_total_nums
	"""
	def create_val_freq_dict(nums: List[int], freq: List[int]) -> Dict[int, int]:
		"""Creates a dictionary of numbers & their frequencies in the list."""
		val_freq_dict = dict()
		for i in range(len(nums)):
			val = val_freq_dict.get(nums[i], 0)
			val += freq[i]
			val_freq_dict[ nums[i]] = val
		
		assert sum(val_freq_dict.values()) == sum(freq)	## check that no duplicate keys in nums
		return val_freq_dict


	def create_total_nums(val_freq_dict: Dict[int, int]) -> List[int]:
		"""Creates list of values from dictionary with values and frequencies."""
		total_nums = []
		for k in sorted(val_freq_dict.keys()):
			total_nums += [int(k) for _ in range(val_freq_dict[k])]

		return total_nums
	

	val_freq_dict = create_val_freq_dict(nums, freq)
	return create_total_nums(val_freq_dict)


##########
# Median
##########

def get_quantile_range(nums: List[int], quantile: int) -> List[int]:
	"""Returns list of integers for the specified quantile range.
	
	n: int, length of list
	nums: list of ints
	median_index: Union[float, int]. Index of the median
	quantile: int, what quantile to return
	"""
	n = len(nums)
	bound = 0 if quantile == 1 else n

	index, r = divmod(n, 2)
	if r and quantile == 3:
		index += 1
	
	b1, b2 = sorted([bound, index])
	return nums[b1: b2]


def calc_median(nums: List[int]) -> Union[float, int]:
	"""Calculates the median from list of numbers."""
	index, r = divmod(len(nums), 2)
	if r:
		return nums[index]
	return sum(nums[index - 1: index + 1]) / 2


##########
# Aux functions
##########

def format_scale(num: Union[float, int]) -> Union[float, int]:
	"""
	If num is float, returns to scale.
	"""
	return "{0:.1f}".format(num)	## Change to scale


##########
# Main
##########

def main():
	## Input
	n, x, f = get_input()

	## Get list of ints
	master_list = get_master_list(x, f)

	## Quantile ranges
	q1_range = get_quantile_range(master_list, quantile=1)
	q3_range = get_quantile_range(master_list, quantile=3)

	## Quantiles
	q1 = calc_median(q1_range)
	q3 = calc_median(q3_range)

	## IQR
	iqr = format_scale(q3 - q1)
	print(iqr)


if __name__ == "__main__":
	main()
