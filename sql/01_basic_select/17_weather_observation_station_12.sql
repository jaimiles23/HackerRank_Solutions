/**
     Solution to weather observation station 12:
     https://www.hackerrank.com/challenges/weather-observation-station-12/problem
 */

SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    (CITY REGEXP '^[^AEIOU]') AND
    (CITY REGEXP '[^AEIOU]$')