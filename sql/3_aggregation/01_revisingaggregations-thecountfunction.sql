-- Solution to [Revising Aggregations - The Count Function](https://www.hackerrank.com/challenges/revising-aggregations-the-count-function)

SELECT
    COUNT(*)
FROM
    CITY
WHERE
    POPULATION > 100000
