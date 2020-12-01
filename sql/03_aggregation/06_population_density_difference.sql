/**
Solution to population difference:
https://www.hackerrank.com/challenges/population-density-difference/problem
 */

SELECT
    MAX(POPULATION) - MIN(POPULATION) AS POP_DIFF
FROM
    CITY
;