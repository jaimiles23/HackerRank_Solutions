/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 12:35:36
 * @modify date 2020-09-05 12:35:36
 * @desc [description]
 */


/*
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

