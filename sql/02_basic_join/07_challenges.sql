/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 16:07:34
 * @modify date 2020-09-05 16:08:15
 * @desc [
    Solution to Challenges:
    https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

Requirements:
    - Columns: hacker_id, name, number_challenges
    - Order by:
        - num challenges DESC
        - hacker_id
        - Only include the maximum number of challenges created

Notes:
    - May need to use MAX() on a subquery to find maximum number of challenges created
 ]
 */


SELECT
    h.hacker_id, h.name,
    COUNT(*) AS num_challenges
FROM 
    Hackers AS h
RIGHT JOIN Challenges AS c
    ON h.hacker_id = c.hacker_id
GROUP BY
    h.hacker_id, h.name
HAVING
    /* Create 2 having conditions: either max, or group with only 1 person*/
    
    /* Max number of challenges */
    num_challenges = (
        SELECT MAX(temp1.count)
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
            ) AS temp1)
    )
    /* In groups of 1 */
    OR num_challenges in (
        SELECT temp2.cnt
        FROM
            (
            SELECT 
                COUNT(hacker_id) AS cnt
            FROM 
                Challenges
            GROUP BY
                hacker_id
            HAVING
                count(temp2.cnt) = 1
            )
    )
ORDER BY
    num_challenges DESC,
    hacker_id ASC
;








