<!-- Solution to [Databases - Differences](https://www.hackerrank.com/challenges/databases-differences) -->

Finding the difference between the two datasets will remove shared elements.


Relation R(A,B,C) has the following tuples:

A B C
- ~~1 2 3~~
- 4 2 3
- ~~4 5 6~~
- ~~2 5 3~~
- 1 2 6

and relation S(A,B,C) has the following tuples:

A B C
- ~~2 5 3~~
- 2 5 4
- ~~4 5 6~~
- ~~1 2 3~~

The differnece (R - S):
A B C
- 4 2 3
- 1 2 6
- 2 5 4

Thus, the answer is:
```
2
3
```