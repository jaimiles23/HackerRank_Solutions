/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 19:27:20
 * @modify date 2020-09-05 19:27:20
 * @desc [
     Solution to Weather Observation Station 2:
     https://www.hackerrank.com/challenges/weather-observation-station-2/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Requirements:
    - SUm of LAT_N, rounded
    - SUM of LONG_W, rounded
]
*/

SELECT
    ROUND(SUM(LAT_N), 2),
    ROUND(SUM(LONG_W), 2)
FROM STATION
;