/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 18:40:27
 * @modify date 2020-09-05 18:40:27
 * @desc [
     Solution to Average population:
     https://www.hackerrank.com/challenges/average-population/problem
 ]
 */

SELECT
    FLOOR(AVG(POPULATION))
FROM
    CITY
;