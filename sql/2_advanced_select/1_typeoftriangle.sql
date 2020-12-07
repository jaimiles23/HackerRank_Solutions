-- Solution to [Type of Triangle](https://www.hackerrank.com/challenges/what-type-of-triangle)

/* Solution 1*/
SELECT
    /* Check is triangle */
    IF(
        (A + B > C) AND (A + C > B) AND (B + C > A),
        /* Then Select triangle type */
            CASE
                WHEN (A = B) AND (A = C)
                    THEN "Equilateral"
                WHEN (A = B) or (B = C) or (A = C)
                    THEN "Isosceles"
                ELSE
                    "Scalene"
            END,
        /* else not triangle */
        "Not A Triangle"
    )
FROM
	TRIANGLES;


/* Solution 2 */
SELECT
    CASE
        WHEN
            (A >= B + C) OR (B >= A + C) OR (C >= A + B)
                THEN "Not A Triangle"
        WHEN (A = B) AND (A = C)
            THEN "Equilateral"
        WHEN (A = B) OR (B = C) OR (A = C)
            THEN "Isosceles"
        ELSE
            "Scalene"
    END
FROM
    TRIANGLES
;