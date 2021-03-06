-- Solution to [Top Competitors](https://www.hackerrank.com/challenges/full-score)

-- Requirements:
-- - columns: hacker_id, hacker_name
-- - where full_score > 1
-- - order by:
--     - challenges > full score, desc
--     - hacker_id, asc

-- Process NOTES:
-- - Because interested in the COUNT of challenges, should use submissions as base table.
-- - Draw out table schemas and PKs & FKs to understand connection.

-- SQL NOTES
-- - When using multi-column select, must also use GROUP BY on same columns



SELECT
    h.hacker_id, h.name
FROM
    Submissions AS s
INNER JOIN Challenges AS c
    ON s.challenge_id = c.challenge_id
INNER JOIN Difficulty AS d
    ON c.difficulty_level = d.difficulty_level
INNER JOIN Hackers AS h
    ON s.hacker_id = h.hacker_id

WHERE
    (s.score = d.score) AND
    (c.difficulty_level = d.difficulty_level)
GROUP BY
    h.hacker_id, h.name
HAVING
    COUNT(*) > 1
ORDER BY
    COUNT(*) DESC,
    s.hacker_id
;