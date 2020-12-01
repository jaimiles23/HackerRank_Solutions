/**
    Solution to weather observation station 13:
    https://www.hackerrank.com/challenges/weather-observation-station-10/problem

    NOTES:
    - Carrot serves as not operator inside brackets. 
 */


SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    CITY REGEXP '[^AEIOU]$'