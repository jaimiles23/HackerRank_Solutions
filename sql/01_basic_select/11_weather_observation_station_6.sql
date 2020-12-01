/**
    Solitions to weather observation station 6:
    https://www.hackerrank.com/challenges/weather-observation-station-6/problem
 */



SELECT
    CITY
FROM
    STATION
WHERE
    CITY REGEXP '^[AEIOU]'