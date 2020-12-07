-- Solution to [The PADS](https://www.hackerrank.com/challenges/the-pads)

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
