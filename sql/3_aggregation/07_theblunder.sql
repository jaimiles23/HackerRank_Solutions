-- Solution to [The Blunder](https://www.hackerrank.com/challenges/the-blunder)

SELECT
    CONVERT(
        INT, 
        CEILING(
            AVG( CONVERT( FLOAT, Salary)) - 
            AVG( CONVERT( FLOAT, REPLACE(Salary, '0', '')))
            )
        )
FROM
    Employees
;

