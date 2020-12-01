/**
    Solution to weather observation station 11:
    https://www.hackerrank.com/challenges/weather-observation-station-11/problem
 */
SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    (CITY REGEXP '^[^AEIOU]') OR
    (CITY REGEXP '[^AEIOU]$')