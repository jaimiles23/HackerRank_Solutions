-- Solution to [Japan Population](https://www.hackerrank.com/challenges/japan-population)


SELECT
    SUM(POPULATION)
FROM
    CITY
WHERE
    COUNTRYCODE = "JPN"
;

