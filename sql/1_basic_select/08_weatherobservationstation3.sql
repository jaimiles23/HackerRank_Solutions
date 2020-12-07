-- Solution to [Weather Observation Station 3](https://www.hackerrank.com/challenges/weather-observation-station-3)

SELECT DISTINCT
    CITY
FROM
    STATION
WHERE
    ID % 2 = 0

