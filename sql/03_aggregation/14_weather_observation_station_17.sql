/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 18:12:47
 * @modify date 2020-09-06 18:12:47
 * @desc [
	Solution to: Weather Observation Station 17
		https://www.hackerrank.com/challenges/weather-observation-station-17

Requirements:
    - ROUND(LONG_W, 4)
    - MIN(LAT_N) > 38.7780

2 different solutions:
	- Subquery
	- Order by, LIMIT 1

Speed complexity:
	- ORDER BY is more costly than an aggregate function -- generally fastest sort is O log(N). 
 ]
 */

/* Solution 1: Subquery */
SELECT
    ROUND(LONG_W, 4)
FROM
    STATION
WHERE
    LAT_N = (
        SELECT
            MIN(LAT_N)
        FROM
            STATION
        WHERE
            LAT_N > 38.7780
    )
    

/* Solution 2: ORDER BY, LIMIT */

SELECT
    ROUND(LONG_W, 4)
FROM
    STATION
WHERE
    LAT_N > 38.778
ORDER BY
    LAT_N
LIMIT
    1
    
