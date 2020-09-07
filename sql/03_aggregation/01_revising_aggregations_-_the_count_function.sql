/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 18:12:25
 * @modify date 2020-09-06 18:12:25
 * @desc [
	Solution to: Revising Aggregations - The Count Function
		https://www.hackerrank.com/challenges/revising-aggregations-the-count-function

NOTE:
        - Check requirements for aggregate function, e.g., COUNT
 ]
 */
SELECT
    COUNT(*)
FROM
    CITY
WHERE
    POPULATION > 100000