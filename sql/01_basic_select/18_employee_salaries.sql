/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 11:51:40
 * @modify date 2020-09-05 11:51:40
 * @desc [
     Solution to Employee Salaries
     https://www.hackerrank.com/challenges/salary-of-employees/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

     NOTES:
     - write requirements of each query to make sure I understand the desire & more clearly document.
 ]
 */

/*
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

