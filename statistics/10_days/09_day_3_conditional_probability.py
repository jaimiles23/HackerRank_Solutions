# -*- coding: utf-8 -*-
"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-16 21:03:42
 * @modify date 2020-09-17 16:30:51
 * @desc [
	 Solution to: Day 3: Conditional Probability
		https://www.hackerrank.com/challenges/s10-mcq-4/problem

This script contains 3 sections:
	- Notes on Conditional Probability
	- Sample Problems
	- Math solution to Conditional Probability Challenge
	- Monte Carlo simulation of Problem

##########
# Notes on Conditional Probability
##########

## Conditional Probability
This is defined as the probability of an event occurring, assuming that one or more other events have already occurred. 
Two events, A and B are considered to be independent if event A has no effect on the probability of event B (i.e. P(B | A) = P(A)). 44

If events A and B are not independent, then we must consider the probability that both events occur. 
This can be referred to as the intersection of events A and B, defined as P(A ∩ B) = P( B | A) * P(B). 
We can then use this definition to find the conditional probability by dividing the probability of the intersection of the two events (A ∩ B) by 
the probability of the event that is assumed to have already occurred (event A):

		P(B | A) = P(A ∩ B) / P(A)

## Bayes' Theorem
Let A and B be two events such that P(A | B) denotes the probability of the occurrence of A given that B has occurred and P(B | A) denotes 
the probability of the occurrence of B given that A has occurred, then:

	P(A | B) = 
		(P(B | A) * P(A) )/ P(B) = 
			(P(B | A) * P(A))	/	(P(B | A)  * P(A) + P(B | Ac)  * P(Ac))

NOTE: c subscript indicates complement.
Words:
- Probability of B, given A, * Probability of A, 
	divided by the Probability of B, given A, times the probability of A + the probability of B given the complement of A, times the complement of A


##########
# Sample Problem 1
##########
Question 1
If the probability of student A passing an exam is 2/7 and the probability of student B *failing* the exam is 3/7, 
then find the probability that at least 1 of the 2 students will pass the exam.

We are given P(A) and P(Bc).


There are 4 possible events in our sample space:

1. A passes the exam and B fails P(A ∩ Bc).
2. B passes the exam and A fails P(B ∩ Ac).
3. A and B both pass the exam P(A ∩ B).
4. A and B both fail the exam P(Ac ∩ Bc).

## Approach 1: Use first 3 events
Calculate the probability of events 1 - 3:

P(at least one passes) = (P(1) + P(2)) - P(3)
	= ((2/7) + (4 / 7)) - (2/7) * (4/7)
	= (6/7) - 8/49 
	= 42/49 - 8/49
	= 34/49

## Approach 2: Use 4th event
Calculate the probability that both will fail the exam, and subtract that from the problem space P(S) to find the complement:

P(at least on passes) = P(S) - P(4)
	= 1 - ((5/7) * 3/7))
	= 1 - (15/49)
	= 34/49


##########
# Sample Problem 2
##########
Historical data shows that it has only rained 5 days per year in some desert region (assuming a 365 day year). 
A meteorologist predicts that it will rain today. When it actually rains, the meteorologist correctly predicts rain 90% of the time. 
When it doesn't rain, the meteorologist incorrectly predicts rain 10% of the time. 
Find the probability that it will rain today.


In this question, the probability of rain today depends on whether or not the meteorolgist predicted it will raid today.
We define the following events:

Event R: It rains today. P(R) =  5/365 = 1/73
Event Rc: It doesn't rain today. P(R) = 360/365 = 72/73
Event M: The meteorologist predicted it will rain today:
	P(M | R) = 9/10
	P(M | Rc) = 1/10

Now we want to find the value of P(R|M):

## Bayes Theorem outlined:
	P(R | M) = 
		(P(M | R) * P(R) )/ P(M) = 
			(P(M | R) * P(R))	/	(P(M | R)  * P(R) + P(M | Rc)  * P(Rc))
				= (9/10 * 1/73) / ( 9/10 * 1/73 + 1/10*72/73)
					= 9/730 /  (9/730 + 72/730)
						= 9 / (9 + 72)
							=	9/81
								=	1/9


##########
# Math solution to Conditional Probability Challenge
##########
Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?

NOTE: This is a famous question in probability theory, taken from here: https://en.wikipedia.org/wiki/Boy_or_Girl_paradox
The wording on this question is a little difficult, but the logic followed makes sense:

Possible families:
1	:	(B, B)
2	:	(B, G)
3	:	(G, B)
4	:	(G, G)

We select only the families with at least one boy, thus we have 3 options:
1	:	(B, B)
2	:	(B, G)
3	:	(G, B)

What is the probability that we select the family with both boys?
1/3!

 ]
 */
"""

##########
# Monte Carlo simulation
##########
"""
This script uses a monte carlo simulation to determine the probability of selecting a family with both boys.
"""

# #########
# Imports
# #########

import random
from typing import List, Set


# #########
# Constants
# #########

CHILDREN = 2
TYPES = ['B', 'G']
NEEDED_GENDER = 'B'
DESIRED_GENDER = 'G'


##########
# Create families
##########
def create_all_possible_families(num_children: int, child_types: List[str]) -> List[List[str]]:
	"""Returns list of list of all possible family combinations.
	
	Referenced: https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/
	"""
	def helper(combos, combo) -> list:
		"""Helper recursive function to return all possible family combinations."""
		if len(combo) == num_children:		## Base case
			combos.append(combo)
			return combos
		
		for child in child_types:
			combos = helper(
				combos,
				combo + [child])
		return combos
	

	return helper([], [])


def remove_without_gender(families: List[List[str]], needed_gender: str) -> List[List[str]]:
	"""Returns families after removing the needed gender from the family.
	
	If the gender is not inside the family, remove the gender.
	"""
	removed = 0
	for i in range(len(families)):
		family = families[i - removed]
		flag_removed_gender = False

		for j in range(len(family)):
			if family[j] == needed_gender:
				del family[j]
				flag_removed_gender = True
			
			if flag_removed_gender:
				break
		
		if not flag_removed_gender:
			del families[i - removed]
			removed += 1

	return families


def get_ratio(families: List[List[str]], gender: str, iterations: int) -> float:
	"""Returns probabily that a child picked from the families is the specified gender."""
	number_picked = 0
	for _ in range(iterations):
		family = random.choice(families)
		child = random.choice(family)
		
		if child == gender:
			number_picked += 1

	return number_picked / iterations


# #########
# Main
# #########

def main():
	possible_families = create_all_possible_families(
		num_children= CHILDREN,
		child_types= TYPES
	)

	allowed_families = remove_without_gender(possible_families, NEEDED_GENDER)

	iterations = 100000
	ratio = get_ratio(allowed_families, NEEDED_GENDER, iterations)
	print(ratio)		# approximates 1/3


if __name__ == "__main__":
	main()
