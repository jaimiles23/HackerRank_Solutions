-- Solution to [Weather Observation Station 13](https://www.hackerrank.com/challenges/weather-observation-station-13)

SELECT
    ROUND( SUM(LAT_N), 4)
FROM
    STATION
WHERE
    LAT_N BETWEEN 38.7880 AND 137.2345
