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

