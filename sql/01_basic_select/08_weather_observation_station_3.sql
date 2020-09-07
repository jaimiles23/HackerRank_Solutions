/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-03 12:36:58
 * @modify date 2020-09-03 12:36:58
 * @desc [
     Solution to Weather Observation Station 3
https://www.hackerrank.com/challenges/weather-observation-station-3/problem

 ]
 */

SELECT DISTINCT
    CITY
FROM
    STATION
WHERE
    ID % 2 = 0
