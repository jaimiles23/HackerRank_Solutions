-- Solution to [Contest Leaderboard](https://www.hackerrank.com/challenges/contest-leaderboard)


/* Create CTE with MAX of submissions? */
WITH top_scores AS (
    SELECT
        hacker_id,
        challenge_id,
        MAX(score) AS high_score
    FROM
        Submissions
    GROUP BY
        hacker_id, challenge_id
)

SELECT
    h.hacker_id,
    h.name,
    SUM(t.high_score) AS total_score
FROM
    Hackers AS h
INNER JOIN top_scores AS t
    ON h.hacker_id = t.hacker_id
GROUP BY
    h.hacker_id, 
    h.name
HAVING
    SUM(t.high_score) > 0
ORDER BY
    total_score DESC,
    h.hacker_id
;
