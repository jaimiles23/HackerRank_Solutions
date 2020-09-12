"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-11 17:23:28
 * @modify date 2020-09-11 17:31:06
 * @desc [
	Solution to: Day 0: Weighted Mean
		https://www.hackerrank.com/challenges/s10-weighted-mean
 ]
 */
"""

##########
# Imports
##########

from typing import List, Union


##########
# Constants
##########

SCALE = 1	# number of decimals


##########
# Weighted Mean
##########




##########
# Format scale
##########

def format_scale(num: Union[int, float]) -> Union[int, float]:
	if isinstance(num, int):
		return num
	
	return round(num, 1)


##########
# Main
##########

def main():
	pass


if __name__ == "__main__":
	main()

