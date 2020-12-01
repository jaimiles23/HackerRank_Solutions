/**
Solution to: Weather Observation Station 16
https://www.hackerrank.com/challenges/weather-observation-station-16

Requirements:
	- Smallest latitude
		- ROUND(,4)
	- greater than 38.7780
 */

SELECT
    ROUND(MIN(LAT_N), 4)
FROM
    STATION
WHERE 
    LAT_N > 38.7780
    ;