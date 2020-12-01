/**
     Solution to Employee Salaries
     https://www.hackerrank.com/challenges/salary-of-employees/

     NOTES:
     - write requirements of each query to make sure I understand the desire & more clearly document.

Requirements:
- Names 
- >2k salary
- less than 10 months
- sort by ID, asc
*/

SELECT
    name
FROM
    Employee
WHERE
    (salary > 2000) AND
    (months < 10)

