/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 18:12:30
 * @modify date 2020-09-06 18:12:30
 * @desc [
	 Solution to: Revising Aggregations - The Sum Function
		https://www.hackerrank.com/challenges/revising-aggregations-sum/

 ]
 */

SELECT
    SUM(POPULATION)
FROM
    CITY
WHERE
    DISTRICT = 'California'