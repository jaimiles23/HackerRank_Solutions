/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 18:12:40
 * @modify date 2020-09-06 18:12:40
 * @desc [
	Solution to: Weather Observation Station 2
		https://www.hackerrank.com/challenges/weather-observation-station-2

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