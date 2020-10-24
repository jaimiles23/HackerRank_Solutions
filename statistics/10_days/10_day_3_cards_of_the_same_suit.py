"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-17 17:11:58
 * @modify date 2020-09-17 17:11:58
 * @desc [
	Solution to: Day 3: Cards of the Same Suit
		https://www.hackerrank.com/challenges/s10-mcq-5/problem

This script contains 3 sections:
1. Notes on permutations and combinations
2. Math solution to Day 3: Cards of the Same Suit problem
3. Monte Carlo simulation of the solution

##########
# Notes
##########
permutations (when order matters) and combinations (when order doesn't matter).

## Permutations
An ordered arrangement of r objects from a set, A, of n objects (where 0 < r <= n) is called an r-element permutation of N. 
You can also think of this as a permutation of A's elements taken r at a time. 
The number of r-element permutations of an n-object set is denoted by the following formula:

nPr = n! / (n - r)!


Note: We define 0! to be 1; otherwise, r = n would result in 0 division error


## Combinations
An unordered arrangement of r objects from a set, A, of n objects (where 0 < r <= A) is called an r-element combination of A. 
You can also think of this as a combination of A's elements taken r at a time.

Because the only difference between permutations and combinations is that combinations are unordered,
we can easily find the number of r-element combinations by dividing out the permutations (r!):

nCr = nPr / r! = n! / (r! * (n - r)!)


When we talk about combinations, we're talking about the number of subsets of size r that can be made from a set of size A. 


##########
# Math Solution
##########
You draw 2 cards from a standard 52-card deck without replacing them. 
What is the probability that both cards are of the same suit?

This solution is simple - but very easy to overthink. I originally thought the answer was a product of dependent events:
(13/52) * (12/51)

However, the first event doesn't matter. You are only interested that the suit of the second card matches the arbitrary suit of the first card.
Thus, the math is:
52/52 * (12/51) = 12/51

 ]
 */

"""

# #########
# Monte Carlo simulation
# #########

# #########
# Imports
# #########

import random
import copy
from typing import List


# #########
# Constants
# #########

DECK_SIZE = 52
NUM_SUITS = 4


##########
# Aux functions
##########
def create_deck(size: int, suits: int) -> List[int]:
	"""Returns a list of ints representing the different number of suites.
	"""
	assert not size % suits		# Check evenly divides

	deck, suit = [], 0
	for i in range(1, DECK_SIZE + 1):
		deck.append(suit)

		if not i % (size / suits):	# increment suit
			suit += 1

	return deck


def get_ratio(deck: list, iterations: int) -> float:
	"""Returns ratio of times that suit chosen from deck is the same"""
	def get_rand_index(deck_size: int) -> int:
		"""Helper func to return random index of deck size"""
		return random.randint(0, deck_size - 1)
	

	same_suit = 0
	for _ in range(iterations):
		temp_deck = copy.deepcopy(deck)

		ind_1, ind_2 = get_rand_index(len(temp_deck)), get_rand_index(len(temp_deck) - 1)
		suit_1 = temp_deck[ind_1]
		del temp_deck[ind_1]
		suit_2 = temp_deck[ind_2]

		if suit_1 == suit_2:
			same_suit += 1
	
	return same_suit / iterations


def main():
	iterations = 100000
	deck = create_deck(DECK_SIZE, NUM_SUITS)
	print(deck)
	ratio = get_ratio(deck, iterations)
	print(ratio)


if __name__ == "__main__":
	main()

