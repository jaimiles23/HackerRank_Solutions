/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 18:36:12
 * @modify date 2020-09-05 18:36:12
 * @desc [
     SOlution to Revising Aggregations - The Sum Function:
     https://www.hackerrank.com/challenges/revising-aggregations-sum/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
 ]
 */

SELECT
    SUM(POPULATION)
FROM
    CITY
WHERE
    DISTRICT = 'California'
