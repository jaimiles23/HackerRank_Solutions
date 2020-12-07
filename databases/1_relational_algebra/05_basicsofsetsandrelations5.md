Solution to [Basics of Sets and Relations #5](https://www.hackerrank.com/challenges/basics-of-sets-and-relational-algebra-5/problem)

[σ](https://en.wikipedia.org/wiki/Relational_algebra#Selection_(%CF%83)) is a unary operation used for selection.

MySQL equivalent:

```sql
Select count(*)
from student
where number<3000;
```

= 2