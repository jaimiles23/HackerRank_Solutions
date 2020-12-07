-- Solution to [Weather Observation Station 17](https://www.hackerrank.com/challenges/weather-observation-station-17)

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
    