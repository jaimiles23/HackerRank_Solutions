/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 17:59:39
 * @modify date 2020-09-06 17:59:39
 * @desc [
	 Solution to: Average Population of Each Continent
		https://www.hackerrank.com/challenges/average-population-of-each-continent/problem

Requirements:
    - Names of continents
    - flooredAverage city populations

Notes:
    - Left join on country code
    - Group by Continent
 ]
 */

SELECT
    COUNTRY.CONTINENT,
    FLOOR(AVG(CITY.POPULATION)) AS avg_pop
FROM
    CITY
INNER JOIN COUNTRY ON
    CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY
    COUNTRY.CONTINENT
;
