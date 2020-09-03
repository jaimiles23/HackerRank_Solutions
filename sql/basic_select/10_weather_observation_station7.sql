/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-03 13:10:24
 * @modify date 2020-09-03 13:10:24
 * @desc [
     Solution to Weather Observation Station 7
https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
 ]
 */

SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    CITY REGEXP '[AEIOU]$'