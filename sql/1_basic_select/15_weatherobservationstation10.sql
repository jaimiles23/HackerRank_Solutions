-- Solution to [Weather Observation Station 10](https://www.hackerrank.com/challenges/weather-observation-station-10)

SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    CITY REGEXP '[^AEIOU]$'
