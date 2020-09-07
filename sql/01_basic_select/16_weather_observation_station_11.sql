/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 11:42:11
 * @modify date 2020-09-05 11:42:11
 * @desc [
    Solution to weather observation station 11:
    https://www.hackerrank.com/challenges/weather-observation-station-11/problem

    NOTE:
    - Realization on how much uppercase is convention in SQL..? 
 ]
 */
SELECT
    DISTINCT CITY
FROM
    STATION
WHERE
    (CITY REGEXP '^[^AEIOU]') OR
    (CITY REGEXP '[^AEIOU]$')