Solution to [Indexes - 3](https://www.hackerrank.com/challenges/indexes-3/problem)

The *Fill Factor* specifies the % of fullness of the leaf level pages of an index. If the Fill Factor is high and insert and index, you may shift indices onto different pages. Consider a fill-factor of 100, where you completely fill leaf level pages. If you insert a row, you must update all subsequent pages. However, if you leave empty space on a page, e.g., with a fill-factor of 50%, you only update the single page.

In design A, the fill-factor is 20%, so you have 80 / 100 indices remaining. In design B, the fill-factor is 40%, and you have 60 / 100 indices remaining. 


Thus, A = 1.33B, or 
80 / 100 = 60 / 100 * 1.33

**Answer**:
A = 1.33B
