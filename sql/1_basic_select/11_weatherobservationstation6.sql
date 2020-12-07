-- Solution to [Weather Observation Station 6](https://www.hackerrank.com/challenges/weather-observation-station-6)

SELECT
    CITY
FROM
    STATION
WHERE
    CITY REGEXP '^[AEIOU]'