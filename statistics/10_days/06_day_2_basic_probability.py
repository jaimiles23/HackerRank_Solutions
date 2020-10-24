"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-13 11:59:20
 * @modify date 2020-09-13 13:12:25
 * @desc [
	 Solution to: Day 2: Basic Probability
		https://www.hackerrank.com/challenges/s10-mcq-1/tutorial

There are 3 sections to this script:
	- Notes on probability from the problem tutorial: https://www.hackerrank.com/challenges/s10-mcq-1/tutorial
	- Mathematic solution to Problem 6 solution
	- Brute force python algorithm to Problem 6 solution


##########
# Notes on probability
##########

## Event, Sample Space, and Probability
n probability theory, an experiment is any procedure that can be infinitely repeated and has a well-defined set of possible outcomes, known as the sample space, s. 
We define an event to be a set of outcomes of an experiment (also known as a subset of s) to which a probability (numerical value) is assigned.

The probability of the occurrence of an event, A, is:
P(A) = (Number of favorable outcome) / (Total number of outcomes)

## Fundamental probability rules
Here are the first two fundamental rules of probability:
	1. Any probability, P(A) , is a number between 0 and 1 (0 <= P(A) <= 1).
	2. The probability of the sample space, S, is 1 (P(S) = 1).

So how do we bridge the gap between the value of P(A) and the sample space P(S)? 
We know that PA() is the probability that event  will occur, then we define P(A')  (the complement of P(A)) to be the probability that event P(A) will not occur. 

If our sample space is composed of the probabilities of P(A)'s occurrence and non-occurrence, we can then say P(A) + P(A') = 1, 
or the sum of all possible outcomes of A in the sample space is equal to 1. This is the third fundamental rule of probability: .

## Question 1:
Find the probability of getting an odd number when rolling a -sided fair die.

Given the above question, we can extract the following:
	- Experiment: rolling a 6-sided die.
	- Sample space (1): .
	- Event (3): that the number rolled is odd (i.e., 1, 3, 5).

P(A) = (number of favorable outcomes) / (total number of outcomes) = P(A) / P(S) = 3/6 = 1/2



## Compound Events, Mutually Exclusive Events, and Collectively Exhaustive Events
Let's consider 2 events: A and B. 
A compound event is a combination of 2 or more simple events. If A and B are simple events, then A u B denotes the occurrence of either A or B. 
Similarly, A n B denotes the occurrence of A and B together.

A and B are said to be mutually exclusive or disjoint if they have no events in common (i.e., A n B = 0  and P(A n B) = 0). 
The probability of any of 2 or more events occurring is the union (u) of events. 
Because disjoint probabilities have no common events, the probability of the union of disjoint events is the sum of the events' individual probabilities.
A and B are said to be collectively exhaustive if their union covers all events in the sample space (i.e., A u B = S and P(A u B) = 1). 

This brings us to our next fundamental rule of probability: if 2 events, A and B, are disjoint, 
then the probability of either event is the sum of the probabilities of the  events (i.e., P(A + B), or P(A) + P(B)).

If the outcome of the first event (A) has no impact on the second event (B), then they are considered to be independent (e.g., tossing a fair coin). 
This brings us to the next fundamental rule of probability: the multiplication rule. 
It states that if two events, A and B, are independent, then the probability of both events is the product of the probabilities for each event (i.e., P(A and B) = P(A) * P(B)). 

The chance of all events occurring in a sequence of events is called the intersection (n) of those events.
	
## Question 2
Find the probability of getting 1 head and 1 tail when  fair coins are tossed.


Given the above question, we can extract the following:
	- Experiment: tossing 2 coins.
	- Sample space (S): The possible outcomes for the toss of 1 coin are {H, T}. 
	As our experiment tosses 2 coins, we have to consider all possible toss outcomes by finding the Cartesian Product of the possible outcomes for each coin: 
	S = {H, T} * {H * T} = {(H, H), (H, T), (T, T), (T, T)}.
	- Event (A n B): that the outcome of 1 toss will be H, and the outcome of the other toss will be T (i.e., P(A) = {(H, T), (T, H)}}

P(A) = (number favorable events) / (total number of events) = P(A) / P(S) = 2 /4 = 1/2


## Question 3
Let A and B be two events such that P(A) = 2/5 and P(B) = 4/5. If the probability of the occurrence of either A or B is 3/5, 
find the probability of the occurrence of both A and B together (i.e., P(A n B)).

We can use our fundamental rules of probability to solve this problem:
	|A u B| = |A| + |B| - |A n B|		## Prob(either or) = prob(A) + prob(b) - prob(both) 	
	P(A u B) = P(A) + P(B) - P(A n B)
	P(A n B) = P(A) + P(B) - P(A u B)
	P(A n B) = 2/5 + 4/5 - 3/5
	P(A n B) = 3/5


##########
# Math Solution
##########

## Information
In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.
	- Experiment: rolling 2 dice
	- Sample space(S) = possible outcomes = 6 * 6 = 36
	- Event P(A + B) <= 9

## Formula:
P(A) = (number favorable events) / (total number events) = P(A) / P(S)

## Implementation
P(A) 	= ( P(1, {1,2,3,4,5,6}) + P(2, {1,2,3,4,5,6}) + P(3, {1,2,3,4,5,6}) + P(4, {1,2,3,4,5}) + P(5, {1,2,3,4}) + P(6, {1,2,3}) ) / 6 ** 2
		= ( 6 + 6 + 6 + 5 + 4 + 3) / 36
		= 30 / 36
		= 5/6
		= 0.833

	* For numbers 1-3, all accompanying die roll <= 9, thus, 100% of roles with these numbers are favored.
	* a role of 4 meets criteria with accompanying roles 1-5, thus resulting in 5 possible permutations, etc.
 ]
 */
"""

# #########
# Imports
# #########

from typing import List


##########
# Information
##########
"""


## Process
- Iterate through all possible rolling combinations and create list of values <= 9
- Divide by number of total events
"""

# #########
# Probability of dice rolls at target
# #########

def get_possible_combinations(num_dice: int, dice_face: int, target: int) -> List[List[int]]:
	"""Returns Cartesian product of all possible dice rolls.
	
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





# #########
# Main
# #########

def main():
	num_dice = 2
	dice_face = 6
	target = 9

	## Get Combinations
	roll_combos = get_possible_combinations(num_dice, dice_face, target)

	## Count combos at target
	num_under_target = 0
	for combo in roll_combos:
		if sum(combo) <= target:
			num_under_target += 1
	
	## Return P(A) / P(S)
	prob = num_under_target / len(roll_combos)
	print( round(prob, 3))


if __name__ == "__main__":
	main()
