/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 11:44:31
 * @modify date 2020-09-05 11:44:31
 * @desc [
     Solution to weather observation station 12:
     https://www.hackerrank.com/challenges/weather-observation-station-12/problem

     NOTES:
     - Change boolean operator from 11.
 ]
 */

SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    (CITY REGEXP '^[^AEIOU]') AND
    (CITY REGEXP '[^AEIOU]$')