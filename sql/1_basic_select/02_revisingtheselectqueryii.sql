-- Solution to [Revising the Select Query II](https://www.hackerrank.com/challenges/revising-the-select-query-2/problem)

SELECT
    NAME
FROM
    CITY
WHERE
    COUNTRYCODE = 'USA' AND
    POPULATION > 120000
