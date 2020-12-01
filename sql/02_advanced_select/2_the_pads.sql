/**
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