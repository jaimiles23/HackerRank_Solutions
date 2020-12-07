-- Solution to [Revising Aggregations - Averages](https://www.hackerrank.com/challenges/revising-aggregations-the-average-function)


SELECT
    AVG(POPULATION)
FROM
    CITY
WHERE
    DISTRICT = 'California'
;
