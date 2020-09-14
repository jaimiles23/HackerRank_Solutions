"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-13 13:26:57
 * @modify date 2020-09-13 18:46:19
 * @desc [
	 Solution to: Day 2: Compound Event Probability
		https://www.hackerrank.com/challenges/s10-mcq-3/problem

This script has 2 parts:
	1. Math Solution
	2. Brute force algorithm implemented in Python


##########
# Math solution
##########

Urn X contains 4 red balls and 3 black balls, 7 balls total.
Urn Y contains 5 red balls and 4 black balls, 9 balls total.
Urn Z contains 4 red balls and 4 black balls, 8 balls total.

## Information
	- Experiment: Given 3 urns with 2 options, what is the compound probability of drawing 2 red and 1 black.
	- Space: 8 * 9 * 8 = 576 possible permutations
	- Formula: sum the  P(of each possible permutation) where you can have 1 black ball.

P(A) 	=	(3/7)(5/9)(1/2) + (4/7)(4/9)(1/2) + (4/7)(5/9)(1/2)
		=	(15/126) + (16/126) + (20/126)
		=	51/126
		=	17/42


##########
# Brute Force algorithm
##########

## Process
	- Use A urns with B black balls and C red balls, represented by (1, 0) respectively
	- Create all possible permutations of urn drawings.
	- Count SUM(combinations) == 1, or where only 1 black ball.
	- Divide by S, (P(S)), or the total number of events.

 ]
 */
"""

##########
# Imports
##########

from typing import List, Tuple


##########
# Instantiate Urns
##########

def create_urns(urn_balls: Tuple[Tuple[int, int]]) -> List[List[int]]:
	"""Returns a list of urns and their number of red and black balls.
	
	Input is a tuple of tuples representing each urn and their number of red and black balls.
	Red and black balls are represented by 0 and 1 respectively
	"""
	urns = []
	for balls in urn_balls:
		# red & black balls, respectively
		urn = [0 for val in range(balls[0])] + [1 for val in range(balls[1])]
		urns.append(urn)
	return urns


##########
# Drawing permutations
##########
"""
TODO
Create recursive solution to generate all possible permutations - don't reference dice rolling.
"""
def get_all_combos(urns: List[List[int]]) -> List[List[int]]:
	"""Returns list of all combinations of drawn balls from urns."""

	def get_balls_from_urn(urn: List[int]) -> int:
		"""Generator function to yield balls from urn."""
		for ball in urn: 
			yield ball

	def recursively_draw_balls(processed_urns: int, ball_combos: List[List[int]]) -> List[List[int]]:
		"""Recursive function to draw balls from urns."""
		## Base case
		if processed_urns == len(urns):
			return ball_combos
		
		new_ball_combos = []

		## Draw first balls
		if not len(ball_combos):
			new_ball_combos = [[val] for val in get_balls_from_urn(urns[processed_urns])]
		
		## Create new lists for each list
		else:
			for combo in ball_combos:
				new_combo = [combo + [val] for val in get_balls_from_urn(urns[processed_urns])]
				new_ball_combos += new_combo
		
		processed_urns += 1
		return recursively_draw_balls(processed_urns, new_ball_combos)
	
	return recursively_draw_balls(0, list())


##########
# Main
##########

def main():
	## Create urns with balls
	urn_balls = (
		(4, 3),			# red, black respectively
		(5, 4),
		(4, 4)
	)
	urns = create_urns(urn_balls)

	## Create all possible permutations
	ball_combos = get_all_combos(urns)

	## Count permutations where SUM == 1, i.e. 1 black ball.
	one_black_ball_permus = 0
	for combo in ball_combos:
		if sum(combo) == 1:
			one_black_ball_permus += 1
	
	## P(A) /P(s)
	p_a = one_black_ball_permus / len(ball_combos)
	print( round(p_a, 5))


if __name__ == "__main__":
	main()

