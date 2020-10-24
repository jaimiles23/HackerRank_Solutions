"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-17 19:39:18
 * @modify date 2020-09-17 19:39:18
 * @desc [
	 Solution to: Day 3: Drawing Marbles
		https://www.hackerrank.com/challenges/s10-mcq-6/problem

This script contains 2 sections:
	1. Math solution to the problem
	2. Monte Carlo simulation of the problem


##########
# Math solution
##########
A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without replacement. 
If the first marble drawn is red, what is the probability that the second marble is blue?

# Facts
- 7 marbles in the bag
- 1st one is always red
- P(B)?

If the first one is always red, we don't calculate the probability of the 1st draw.
Thus, we use the 6 remaining marbles.
	P(B) = 4/6
		= 2/3

 ]
 */
"""
##########
# Monte Carlo
##########

##########
# Imports
##########

from typing import List
import random


##########
# Constants
##########

MARBLE_DICT = {
	'r'	:	3,
	'b'	:	4
}
FIRST_MARBLE = 'r'
SECOND_MARBLE = 'b'


##########
# Aux
##########
def create_marble_bag(marbles: dict) -> List[str]:
	"""Returns list of marbles to draw from."""
	bag = []
	for k, v in marbles.items():
		m = [k for _ in range(v)]
		bag += m
	return bag


def remove_first_marble(bag: List[str], marble: str) -> List[str]:
	"""Returns bag after removing marble."""
	bag.remove(marble)
	return bag


def check_second_marble(bag: List[str], marble: str) -> bool:
	"""Returns boolean if sample from bag is the marble."""
	return random.choice(bag) == marble


def get_ratio(bag: List[str], marble: str, iterations: int) -> float:
	"""Returns ratio of times sample from bag is marble."""
	was_marble = 0
	for _ in range(iterations):
		if check_second_marble(bag, marble):
			was_marble += 1
	return was_marble / iterations


##########
# Main
##########

def main():
	bag = create_marble_bag(MARBLE_DICT)
	bag = remove_first_marble(bag, FIRST_MARBLE)

	iterations =  1000000
	ratio = get_ratio(bag, SECOND_MARBLE, iterations)
	print(ratio)


if __name__ == "__main__":
	main()
