-- Solution to [African Cities](https://www.hackerrank.com/challenges/african-cities)

SELECT
    CITY.NAME
FROM
    CITY
INNER JOIN COUNTRY ON
    CITY.COUNTRYCODE = COUNTRY.CODE
WHERE
    COUNTRY.CONTINENT = "Africa"
;
