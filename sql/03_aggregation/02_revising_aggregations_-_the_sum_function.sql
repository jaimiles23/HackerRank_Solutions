/**
Solution to: Revising Aggregations - The Sum Function
https://www.hackerrank.com/challenges/revising-aggregations-sum/
 */

SELECT
    SUM(POPULATION)
FROM
    CITY
WHERE
    DISTRICT = 'California'