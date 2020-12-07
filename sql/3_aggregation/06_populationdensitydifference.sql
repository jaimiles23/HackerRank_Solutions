-- Solution to [Population Density Difference](https://www.hackerrank.com/challenges/population-density-difference)

SELECT
    MAX(POPULATION) - MIN(POPULATION) AS POP_DIFF
FROM
    CITY
;
