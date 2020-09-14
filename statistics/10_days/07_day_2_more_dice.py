"""
/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-13 13:13:52
 * @modify date 2020-09-13 13:24:58
 * @desc [
	Solution to: Day 2: More Dice
		https://www.hackerrank.com/challenges/s10-mcq-2/problem

Notes on basic probability available in #6: Day 2 Basic probability.

This script contains two parts:
	1. Math solution
	2. Brute force algorithm solution implemented in Python

##########
# Math solution
##########

## Information
	- Experiment: Roll 2 die and find the probability that sum == 6 with differnt die faces
	- Sample Space: possible outcomes == 36
	- Event: P( (A !+ B) n (A + B == 6))
	- Formula: P(number favorable events) / P(total number of events) = P(A) / P(S)

P(A) 	= ( P([1, 5]), P( [2, 4])) / S				# prob of rolling (1, 5) or (2, 4) divided by S
		= 2 + 2 / 36
		= 4 / 36
		= 1 / 9


## NOTE: 
- For this solution, I use the def _get_possible_combinations() function defined in the 06_day_2_basic_probability.py solution.
 ]
 */
"""

##########
# Imports
##########

from typing import List


##########
# Probability of unique dice rolls at target
##########

def prob_dice_unique_and_equal_target(num_dice: int, dice_face: int, target: int) -> None:
	"""Prints probability that rolling 2 dice will return less than or equal to 9."""

	def _get_possible_combinations() -> List[List[int]]:
		"""RReturns Cartesian product of all possible dice rolls.
		
		Uses two helper functions:
			- get_possible_rolls, generator func to yield all die rolls.
			- recurse_roll_combos, helper recursion to create combinations for `num_dice`
		"""
		def get_possible_rolls(dice_face: int) -> int:
			"""Generator funct to yield possible rolls."""
			for i in range(1, dice_face + 1): yield i
		

		def recurse_roll_combos(processed_dice: int, all_roll_combos: list) -> List[List[int]]:
			"""Helper func to recurse through all dice."""
			if processed_dice == num_dice:		## Base case
				return all_roll_combos
			
			new_roll_combos = []
			for roll in all_roll_combos:
				roll_combo = [roll + [val] for val in get_possible_rolls(dice_face)]
				new_roll_combos += (roll_combo)
			
			processed_dice += 1
			return recurse_roll_combos(processed_dice= processed_dice, all_roll_combos = new_roll_combos)

		
		first_rolls = [[val] for val in get_possible_rolls(dice_face)]
		roll_combinations = recurse_roll_combos( 1, first_rolls)


		assert (len(roll_combinations) == dice_face ** num_dice)
		return roll_combinations
	

	## Get Combinations
	roll_combos = _get_possible_combinations()

	## Count unique combos in target
	num_at_target = 0
	for combo in roll_combos:

		flag_unique = True
		for c in combo:
			if combo.count(c) > 1:
				flag_unique = False
				break
		
		if flag_unique and sum(combo) == target:
			num_at_target += 1
	
	## Return P(A) / P(S)
	prob = num_at_target / len(roll_combos)
	print( round(prob, 3))


##########
# Main
##########

def main():
	num_dice = 2
	dice_face = 6
	target = 6

	prob_dice_unique_and_equal_target(num_dice, dice_face, target)


if __name__ == "__main__":
	main()


