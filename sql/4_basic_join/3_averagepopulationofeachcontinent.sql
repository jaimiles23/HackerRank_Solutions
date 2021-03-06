-- Solution to [Average Population of Each Continent](https://www.hackerrank.com/challenges/average-population-of-each-continent/problem)

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
