/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 18:12:50
 * @modify date 2020-09-06 18:12:50
 * @desc [
	Solution to: Weather Observation Station 20
		https://www.hackerrank.com/challenges/weather-observation-station-20

Median is the middle value of a sorted listed of values.

Requirements:
    - LAT_N
    - Sorted

Process:
    - Create row numbers for LAT_N, both ASC & DESC
    - For an ODD length col, find where ASC == DESC
    - For an EVEN length col, select both values above and below
 ]
 */

SELECT
    ROUND( AVG(LAT_N), 4)
FROM
    (       /* Create row numbers for order by asc & desc. Use for intersection */
    SELECT
        *, 
        ROW_NUMBER() OVER (ORDER BY LAT_N DESC) AS D_LAT_N,
        ROW_NUMBER() OVER (ORDER BY LAT_N ASC) AS A_LAT_N
    FROM
        STATION
    ) AS temp1
WHERE
    /* equal value for odd lists, or +/- 1 for even lists */
    D_LAT_N IN (A_LAT_N -1, A_LAT_N, A_LAT_N + 1)
    ;
