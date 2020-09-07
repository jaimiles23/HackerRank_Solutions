/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 18:43:05
 * @modify date 2020-09-05 18:43:05
 * @desc [
     Solution to The Blunder:
     https://www.hackerrank.com/challenges/the-blunder/problem

Process Notes:
    - Must include CONVERT() in both averages to get correct answer. Otherwise average is off... I would not expect this functionality from average?

SQL Notes:
    - Two ways to change data type: CONVERT(type, data) and CAST(DATA AS TYPE)
        - Prefer convert because follows convention of OOP parameters
    - Replace() will automatically convert other data types to string.
 ]
 */

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

