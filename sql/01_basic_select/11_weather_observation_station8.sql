/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 11:32:12
 * @modify date 2020-09-05 11:32:12
 * @desc [
     Solution to weather observation station 8:
     https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true

     NOTE:
     - need index name before REGEXP.
     - Can use boolean operators with REGEXP
 ]
 */


SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    (CITY REGEXP '^[AEIOU]') AND
    (CITY REGEXP '[AEIOU]$')