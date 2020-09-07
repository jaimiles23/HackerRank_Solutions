/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 18:12:34
 * @modify date 2020-09-06 18:12:34
 * @desc [
	 Solution to: Revising Aggregations - Averages
		https://www.hackerrank.com/challenges/revising-aggregations-the-average-function

 ]
 */

SELECT
    AVG(POPULATION)
FROM
    CITY
WHERE
    DISTRICT = 'California'
;
