-- Solution to [Challenges](https://www.hackerrank.com/challenges/challenges/problem)
-- Requirements:
-- - Columns: hacker_id, name, number_challenges
-- - Order by:
-- - num challenges DESC
-- - hacker_id
-- - Only include the maximum number of challenges created

-- Notes:
-- - May need to use MAX() on a subquery to find maximum number of challenges created
-- - Used TWO solutions. 
-- - Solution 1: Uses temporary queries inside HAVING.
-- - Solution 2: Uses CTE to create master data and filters the CTE inside of where clauses.

-- HackerRank Note:
-- - MUST USE MS SQL SERVER To use CTEs with MySQL.


/* Solution 1: Using temporary subqueries for each condition of displaying the names. */
SELECT
    c.hacker_id, h.name, 
    COUNT(c.hacker_id) AS c_count
FROM
    Hackers AS h
INNER JOIN Challenges AS c
    ON c.hacker_id = h.hacker_id

GROUP BY h.hacker_id, h.name

HAVING
    c_count = (
        SELECT 
            MAX(temp1.cnt)
        FROM
            (
                SELECT 
                    COUNT(hacker_id) AS cnt
                FROM
                    Challenges
                GROUP BY
                    hacker_id
                ORDER BY 
                    hacker_id
            ) AS temp1
                )
    OR c_count IN (
        SELECT 
            temp2.cnt
        FROM 
        (
            SELECT
                COUNT(*) AS cnt
            FROM
                Challenges
            GROUP BY
                hacker_id
        ) AS temp2
        GROUP BY
            temp2.cnt
        HAVING
            COUNT(temp2.cnt) = 1
        )
ORDER BY
    c_count DESC,
    c.hacker_id
;


/* Solution 2: CTE to count submissions per user */

/* Create CTE with all data */
WITH data (id, name, s_count) AS (
    SELECT
        h.hacker_id AS id,
        h.name AS name,
        COUNT(c.hacker_id) AS s_count
    FROM
        Hackers AS h
    INNER JOIN Challenges AS c
        ON h.hacker_id = c.hacker_id
    GROUP BY
        h.hacker_id, h.name
)

SELECT
    id, name, s_count
FROM
    data
WHERE
    (s_count = (    /* NOTE: must have SELECT inside parenthesis to evaluate */
        SELECT MAX(data.s_count) FROM data))
    OR
    (s_count IN (
        SELECT
            s_count
        FROM
            data
        GROUP BY
            s_count
        HAVING
            COUNT(s_count) = 1
    ))
ORDER BY
    s_count DESC,
    id ASC
;