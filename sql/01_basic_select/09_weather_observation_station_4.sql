/**
    Solution to Weather Observation Station 4:
    https://www.hackerrank.com/challenges/weather-observation-station-4/problem

    NOTES:
    - Distinct can be used for a single table attribute when inside an aggregate function.

 */

 SELECT
    COUNT(CITY) - COUNT( DISTINCT CITY)
FROM
    STATION
