/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-03 12:23:58
 * @modify date 2020-09-03 12:23:58
 * @desc [
     Solution to: Revising the Select Query I: https://www.hackerrank.com/challenges/revising-the-select-query/problem
 ]
 */


SELECT 
    *
FROM 
    CITY
WHERE
    COUNTRYCODE = 'USA' AND 
    POPULATION > 100000
