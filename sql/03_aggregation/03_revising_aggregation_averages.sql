/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 18:37:32
 * @modify date 2020-09-05 18:37:32
 * @desc [
     Solution to Revising Aggregations - Averages:
     https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
 ]
 */

SELECT
    AVG(POPULATION)
FROM
    CITY
WHERE
    DISTRICT = 'California'
;