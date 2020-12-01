/**
     Solution to weather observation station 9:
     https://www.hackerrank.com/challenges/weather-observation-station-9/problem

     NOTES:
     - REGEXP character for STARTS and EXCLUDES are the same. Difference is their placement inside brackets (inside= exclusion).FROM

 */


SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    CITY REGEXP '^[^AEIOU]'