-- Solution to [Weather Observation Station 4](https://www.hackerrank.com/challenges/weather-observation-station-4)

SELECT
    COUNT(CITY) - COUNT( DISTINCT CITY)
FROM
    STATION
