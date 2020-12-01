/**
     Solution to weather observation station 8:
     https://www.hackerrank.com/challenges/weather-observation-station-8/problem

     NOTE:
     - need index name before REGEXP.
     - Can use boolean operators with REGEXP
 */


SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    (CITY REGEXP '^[AEIOU]') AND
    (CITY REGEXP '[AEIOU]$')