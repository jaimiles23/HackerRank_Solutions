/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-03 12:48:01
 * @modify date 2020-09-03 12:48:01
 * @desc [
     Solution to Weather Observation Station 5:
     https://www.hackerrank.com/challenges/weather-observation-station-5/problem

     NOTE:
     - Separated this solution into 2 separate queries. Re-arranged the order and took the top result.
 ]
 */

SELECT
    CITY,
    LENGTH(CITY) 
FROM 
    STATION
ORDER BY
    LENGTH(CITY),
    CITY
    ASC
LIMIT 1;

SELECT
    CITY,
    LENGTH(CITY)
FROM
    STATION
ORDER BY
    LENGTH(CITY)
    DESC
LIMIT 1;
