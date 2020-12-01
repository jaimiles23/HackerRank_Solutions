/**
Solution to: Weather Observation Station 19
    https://www.hackerrank.com/challenges/weather-observation-station-19

In mathematics, the Euclidean distance or Euclidean metric is the "ordinary" straight-line distance between two points in Euclidean space.
dist((x1, y1), (x2, y2)) = √(x1 - x2)² + (y1 - y2)²

Requirements:
    - Find MIN/MAX of LAT_N and LONG_W
    - Calc Euclidean distance, to 4 decimals	
 */


SELECT
    ROUND(
        SQRT(
            POWER(MIN(LAT_N) - MAX(LAT_N), 2) + 
            POWER(MIN(LONG_W) - MAX(LONG_W), 2)
            )
        , 4)
FROM
    STATION


