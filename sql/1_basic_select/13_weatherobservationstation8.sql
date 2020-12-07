-- Solution to [Weather Observation Station 8](https://www.hackerrank.com/challenges/weather-observation-station-8/problem)

SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    (CITY REGEXP '^[AEIOU]') AND
    (CITY REGEXP '[AEIOU]$')

