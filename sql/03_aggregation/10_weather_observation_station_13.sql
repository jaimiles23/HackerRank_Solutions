/**
Solution to:
https://www.hackerrank.com/challenges/weather-observation-station-13/problem


Requirements: 
    - Sum of LAT_N greater than 38.7880 and less than 137.2345

SQL process:
    Need to use IF function inside SUM
*/

SELECT
    ROUND( SUM(LAT_N), 4)
FROM
    STATION
WHERE
    LAT_N BETWEEN 38.7880 AND 137.2345
        