/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 18:42:34
 * @modify date 2020-09-05 18:42:34
 * @desc [
    Solution to population difference:
    https://www.hackerrank.com/challenges/population-density-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
    
 ]
 */

SELECT
    MAX(POPULATION) - MIN(POPULATION) AS POP_DIFF
FROM
    CITY
;