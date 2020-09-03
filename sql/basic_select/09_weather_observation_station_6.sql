/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-03 13:07:26
 * @modify date 2020-09-03 13:07:26
 * @desc [
     Solitions to weather observation station 6:
     https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
 ]
 */



SELECT
    CITY
FROM
    STATION
WHERE
    CITY REGEXP '^[AEIOU]'