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


## Approach 2: Use 4th event


##########
# Sample Problem 2
##########




 ]
 */
"""

