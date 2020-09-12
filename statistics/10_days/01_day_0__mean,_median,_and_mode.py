"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-11 16:24:44
 * @modify date 2020-09-11 17:21:36
 * @desc [Solution to: Day 0: Mean, Median, and Mode
		https://www.hackerrank.com/challenges/s10-basic-statistics/problem]

NOTE:
	- Print on separate lines (mean, median, mode)
	- Scale of 1 decimal place
	- With multiple mode values, select min.
 */
"""

##########
# Imports
##########

from typing import List, Union
from collections import Counter			# used to count instances for mode


##########
# Constants
##########

SCALE = 1			# scale refers to number of decimal places


##########
# Get Input
##########

n = int(input())
nums = sorted(int(num) for num in input().split())



##########
# Measures of Central Tendency funcs
##########

def calc_mean(nums: List[int], n: int) -> Union[int, float]:
	"""Returns mean of nums list with n elements."""
	return format_scale( sum(nums) / n)


def calc_median(nums: List[int], n: int) -> Union[int, float]:
	"""Returns median of nums list with n elements."""
	mid, is_odd = divmod(len(nums), 2)
	if is_odd:
		median = nums[mid]
	else:
		median = calc_mean( nums[mid - 1: mid + 1], 2)
	return format_scale(median)


def calc_mode(nums: List[int], n: int) -> int:
	"""Returns mode of nums list.
	
	Uses auxiliary get_mode_ties func.
	"""
	def get_mode_ties(num_counts: dict, max_freq: int) -> int:
		"""Generator function to return contenders for mode in dict."""
		for num, count in num_counts.items():
			if count == max_freq:
				yield num


	num_counts = Counter(nums)
	max_freq = num_counts[ max( num_counts, key = num_counts.get)]

	return min(list(get_mode_ties(num_counts, max_freq)))


##########
# Aux Functions
##########

def format_scale(num: Union[int, float]) -> float:
	"""Returns float number ."""
	if isinstance(num, int):
		return num
	return round(num, SCALE)


##########
# Main
##########

def main():
	measure_central_tendency = (
		calc_mean,
		calc_median,
		calc_mode
	)
	for measure in measure_central_tendency:
		print(measure(nums, n))


if __name__ == "__main__":
	main()
