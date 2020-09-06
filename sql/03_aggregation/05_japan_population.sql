/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 18:41:20
 * @modify date 2020-09-05 18:41:20
 * @desc [
    Solution to Japanese Population:
    https://www.hackerrank.com/challenges/japan-population/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

 ]
 */


SELECT
    SUM(POPULATION)
FROM
    CITY
WHERE
    COUNTRYCODE = "JPN"
;
