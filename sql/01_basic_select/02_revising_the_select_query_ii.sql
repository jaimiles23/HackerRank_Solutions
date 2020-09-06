/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-03 12:25:26
 * @modify date 2020-09-03 12:25:26
 * @desc [
     Solution to revising the select query II: https://www.hackerrank.com/challenges/revising-the-select-query-2/
 ]
 */


SELECT
    NAME
FROM
    CITY
WHERE
    COUNTRYCODE = 'USA' AND
    POPULATION > 120000