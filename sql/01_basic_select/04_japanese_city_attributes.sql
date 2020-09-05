/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-03 12:31:24
 * @modify date 2020-09-03 12:31:24
 * @desc [
     Solution to Japanese City Attributes: https://www.hackerrank.com/challenges/japanese-cities-attributes/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
 ]
 */

SELECT
    NAME
FROM
    CITY
WHERE
    COUNTRYCODE = 'JPN'
