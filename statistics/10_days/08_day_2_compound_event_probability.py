"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-13 13:26:57
 * @modify date 2020-09-13 13:26:57
 * @desc [
	 Solution to: Day 2: Compound Event Probability
		https://www.hackerrank.com/challenges/s10-mcq-3/problem

## Information
	- Experiment: Given 3 urns with 2 options, what is the compound probability of drawing 2 red and 1 black.
	- Space: number of combinations, 2 * 2 * 2, with different probabilities of each.
	- P(A) = P()

## Process
	- Use A urns with B black balls and C red balls, represented by (1, 0) respectively
	- Create all possible permutations of urn drawings.
	- Count SUM(combinations) == 2
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
		urn = [0 for val in balls[0]] + [1 for val in balls[1]]
		urns.append(urn)
	return urns


##########
# Drawing permutations
##########
"""
TODO
Create recursive solution to generate all possible permutations - don't reference dice rolling.
"""







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




if __name__ == "__main__":
	main()

