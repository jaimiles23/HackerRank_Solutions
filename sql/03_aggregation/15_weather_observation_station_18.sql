/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 18:12:48
 * @modify date 2020-09-06 18:12:48
 * @desc [
	 Solution to: Weather Observation Station 18
		https://www.hackerrank.com/challenges/weather-observation-station-18/problem

Manhatten Distance: The distance between two points measured along axes at right angles. 
In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|.

 ]
 */


SELECT
    ROUND(
        ABS(MAX(LAT_N) - MIN(LAT_N)) + 
        ABS(MAX(LONG_W) - MIN(LONG_W))
        , 4)
FROM
    STATION
