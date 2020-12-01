/**
Solution to: Ollivander's Inventory
https://www.hackerrank.com/challenges/harry-potter-and-wands/problem

Requirements:
    - Columns: id, age, coins_needed, power wand
    - where wand <> evil
    - Order by:
        - Power Desc
        - Age Desc

Process:
    - Problem requirements don't clearly explain that looking for the minimum of each wand's power and age groupings.
 */


SELECT
    w.id, p.age, w.coins_needed, w.power
FROM
    Wands AS w
INNER JOIN Wands_Property AS p
    ON w.code = p.code
WHERE
    (p.is_evil = 0) AND
    /* Find min of subtable group to compare with each record */
    (W.coins_needed = 
        (   SELECT 
                MIN(coins_needed)
            FROM 
                Wands AS w1
            INNER JOIN Wands_Property AS p1
                ON w1.code = p1.code
            WHERE
                (w1.power = w.power) AND
                (p1.age = p.age)
         ))
ORDER BY
    w.power DESC,
    p.age DESC
;