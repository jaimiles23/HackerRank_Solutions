/**
Solution to:
https://www.hackerrank.com/challenges/weather-observation-station-14/problem
     
Requirements:
    - greatest value
    - less than 137.2345
    - Truncate to 4 decimal places

NOTES:
    - Can use TRUNCATE function instead of round.
 */


SELECT
    TRUNCATE(MAX(LAT_N), 4)
FROM
    STATION
WHERE
    (LAT_N < 137.2345)


