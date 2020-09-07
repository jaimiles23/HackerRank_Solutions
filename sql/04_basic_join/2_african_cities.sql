/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 17:59:37
 * @modify date 2020-09-06 17:59:37
 * @desc [
	 Solution to: African Cities
		https://www.hackerrank.com/challenges/african-cities

Requirements:
    - City names
    - Where Continent is Africa

Notes:
    - Left join City.CountryCode and Country.Code
    - When interested in matches, can use either inner joiin OR left join.
 ]
 */

SELECT
    CITY.NAME
FROM
    CITY
INNER JOIN COUNTRY ON
    CITY.COUNTRYCODE = COUNTRY.CODE
WHERE
    COUNTRY.CONTINENT = "Africa"
;
