/**
Solution to: African Cities
https://www.hackerrank.com/challenges/african-cities

Requirements:
    - City names
    - Where Continent is Africa

Notes:
    - Left join City.CountryCode and Country.Code
    - When interested in matches, can use either inner joiin OR left join.
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
