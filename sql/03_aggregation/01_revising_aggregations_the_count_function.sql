/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 18:34:16
 * @modify date 2020-09-05 18:34:16
 * @desc [
     Solution to Revising Aggregations: The count function:
     https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem

     NOTE:
        - Check requirements for aggregate function, e.g., COUNT
 ]
 */

 SELECT
    COUNT(*)
FROM
    CITY
WHERE
    POPULATION > 100000
