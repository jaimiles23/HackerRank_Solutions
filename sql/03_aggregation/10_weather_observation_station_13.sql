/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 19:34:54
 * @modify date 2020-09-05 19:34:54
 * @desc [
     Solution to weather observation station 13
     https://www.hackerrank.com/challenges/weather-observation-station-13/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

    /*
Requirements: 
    - SUm of LAT_N greater than 38.7880 and less than 137.2345

SQL process:
    Need to use IF function inside SUM
*/
 ]
 */

SELECT
    ROUND( SUM(LAT_N), 4)
FROM
    STATION
WHERE
    LAT_N BETWEEN 38.7880 AND 137.2345
        