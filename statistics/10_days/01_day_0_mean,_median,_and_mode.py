# Solution to: [Day 0: Mean, Median, and Mode](https://www.hackerrank.com/challenges/s10-basic-statistics/problem)
#

# <h1 id="tocheading">Table of Contents</h1>
# <div id="toc"></div>

# + language="javascript"
# $.getScript('https://kmahelona.github.io/ipython_notebook_goodies/ipython_notebook_toc.js')
# -

# # Wiki definition
# In statistics, a central tendency (or measure of central tendency) is a central or typical value for a probability distribution.
#
# The most common measures of central tendency are the arithmetic mean, the median, and the mode. 
# A middle tendency can be calculated for either a finite set of values or for a theoretical distribution, such as the normal distribution. 
# Occasionally authors use central tendency to denote "the tendency of quantitative data to cluster around some central value."
#
# The central tendency of a distribution is typically contrasted with its dispersion or variability; 
# dispersion and central tendency are the often characterized properties of distributions. 
# Analysis may judge whether data has a strong or a weak central tendency based on its dispersion.
#

# # Solution
# 	- Print on separate lines (mean, median, mode)
# 	- Scale of 1 decimal place
# 	- With multiple mode values, select min.
#

# ## Imports

from collections import Counter  # used to count instances for mode
from typing import List, Tuple, Union

# ## Constants

SCALE = 1	# scale refers to number of decimal places


# ## Input

def get_input() -> Tuple[int, list]:
    """Returns tuple of input:
    n: int, length of list.
    nums: list, nums to use.
    """
    n = int(input())
    nums = sorted(int(num) for num in input().split())
    return (n, nums)


# ## Measures of Central Tendency

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


# ## Scale function

def format_scale(num: Union[int, float]) -> float:
	"""Returns float number ."""
	if isinstance(num, int):
		return num
	return round(num, SCALE)


# ## Main

def main():
	measure_central_tendency = (
		calc_mean,
		calc_median,
		calc_mode
	)
	n, nums = get_input()
	for measure in measure_central_tendency:
		print(measure(nums, n))


if __name__ == "__main__":
	main()
