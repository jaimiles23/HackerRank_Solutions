/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 11:38:31
 * @modify date 2020-09-05 11:38:31
 * @desc [
    Solution to weather observation station 13:
    https://www.hackerrank.com/challenges/weather-observation-station-10/problem

    NOTES:
    - Carrot serves as not operator inside brackets. 
 ]
 */


SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    CITY REGEXP '[^AEIOU]$'