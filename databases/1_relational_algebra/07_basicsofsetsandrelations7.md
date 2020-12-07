Solution to [Basics of Sets and Relations #7](https://www.hackerrank.com/challenges/basics-of-sets-and-relational-algebra-7/problem)

**Student**
```
Student Name        Number  Sex  
Nina                3412    F 
Mike                1234    M  
Nelson              2341    F  
```

**Teaching Assistants**
```
Subject     ID
Physics     3412
Chemistry   1111
Mathematics 2341  
```

`Student ⊳⊲(Number=ID) Teaching Assistants`

[Natural join](https://en.wikipedia.org/wiki/Relational_algebra#Natural_join_(%E2%8B%88)) (⋈) is a binary operator. The result of the natural join is the set of all combinations of tuples in R and S that are equal on their common attribute names. 

Thus, this result returns joined rows. SQL equivalent
```sql
SELECT
    *
FROM
    Students
INNER JOIN ON
    Student.Number == Teaching Assistants.ID
```
= 2 rows 

_Note_: Mike & chemistry do not pair.

