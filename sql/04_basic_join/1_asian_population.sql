/**
Solution to: Asian Population
https://www.hackerrank.com/challenges/asian-population

NOTES:
    - Requirements to understand the metrics desired (SUM)
    - left join uses the left table as the FROM, and the right table is after left join.

Requirements:
    - SUM populations
    - WHERE contintent is ASIA

NOTES:
    - JOIN CITY.CountryCode and COUNTRY.Code
 */

SELECT
    SUM(CITY.POPULATION)
FROM
    CITY
LEFT JOIN COUNTRY ON
    CITY.COUNTRYCODE = COUNTRY.CODE
WHERE
    COUNTRY.CONTINENT = 'Asia'