/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 13:13:49
 * @modify date 2020-09-05 13:13:49
 * @desc [
    Solution to Top Competitors:
    https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

Requirements:
    - columns: hacker_id, hacker_name
    - where full_score > 1
    - order by:
        - challenges > full score, desc
        - hacker_id, asc

NOTES:
    - Because interested in the COUNT of challenges, should use submissions as base table.
    - Join info from other tables
    - count statements on hackers

 ]
 */


SELECT
    h.hacker_id,
    h.name
FROM
    Submissions AS s
INNER JOIN Challenges AS c
    ON s.challenge_id = c.challenge_id
INNER JOIN Difficulty AS d
    ON c.difficulty_level = d.difficulty_level
INNER JOIN Hackers AS h
    ON s.challenge_id = h.hacker_id
WHERE
    (s.score = d.score) AND
    (c.difficulty_level = d.difficulty_level)
GROUP BY 
    h.hacker_id
    HAVING
        COUNT(s.hacker_id) > 1
ORDER BY 
    COUNT(*) DESC,
    h.hacker_id ASC
;
