/**
Solution to Japanese Population:
https://www.hackerrank.com/challenges/japan-population/problem
 */


SELECT
    SUM(POPULATION)
FROM
    CITY
WHERE
    COUNTRYCODE = "JPN"
;
