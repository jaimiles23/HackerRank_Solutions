Solution to [Databases - Natural Joins](https://www.hackerrank.com/challenges/databases-natural-joins/problem)

Relation R(A,C) has the following tuples:
```
A : C
3,3
16,4
12,3
3,15
27,1
```

Relation S(B,C,D) has the following tuples:
```
B : C : D
50,1,6
1,55,8
4,3,9
```

The following tuple is in the result of the natural join between R and S where tuples are structured as (A,B,C,D):

27, **X, Y, Z**


**Process**

In this case, C is the foriegn key between the two tables. Thus, the row from R(A, C) is `27, 1` and S(B, C, D) is `50, 1, 6`. Thus, the form (A, B, C, D) is `27, 50, 1, 6`.


**Answer**

50
1
6
