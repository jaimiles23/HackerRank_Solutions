/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 11:45:20
 * @modify date 2020-09-06 11:45:20
 * @desc [
     Solution to weather observation station 14:
     https://www.hackerrank.com/challenges/weather-observation-station-14/problem?isFullScreen=true
     
Requirements:
    - greatest value
    - less than 137.2345
    - Truncate to 4 decimal places

NOTES:
    - Can use TRUNCATE function instead of round.
 ]
 */


SELECT
    TRUNCATE(MAX(LAT_N), 4)
FROM
    STATION
WHERE
    (LAT_N < 137.2345)


