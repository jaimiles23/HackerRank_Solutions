/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-07 16:51:56
 * @modify date 2020-09-07 16:51:56
 * @desc [
	Solution to: The PADS
		https://www.hackerrank.com/challenges/the-pads

Requirements:
    Query 1
        - Names, and first letter of each occupation
        - ordered by name, Asc
    Query 2
        - Number of each occupation
            output: There are a total of [occupation_count] [occupation]s.
        - Order by
            number

Needed SQL string operators:
    - CONCAT
    - LEFT
    - LOWER
 ]
 */

/* Query 1 */
SELECT
    CONCAT(Name, "(", LEFT(Occupation, 1), ")")
FROM
    OCCUPATIONS
ORDER BY
    Name
;

/* Query 2 */
SELECT
    CONCAT("There are a total of ", COUNT(*), " ", LOWER(Occupation), "s.")
FROM
    OCCUPATIONS
GROUP BY
    Occupation
ORDER BY 
    COUNT(*) ASC,
    Occupation ASC
;