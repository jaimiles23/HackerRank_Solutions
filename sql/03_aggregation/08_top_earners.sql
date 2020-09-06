/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 19:24:10
 * @modify date 2020-09-05 19:24:10
 * @desc [
     Solution to Top Earners:
     https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
     
 ]
Requirements
    - max total earnings
    - number of employees who made that
    
Steps:
    - Calculate total earnings, take max
    - Group by total earnings
    - Take top result
*/

SELECT
    salary * months AS total_earnings,
    COUNT(*) as num_employees
FROM
    Employee
GROUP BY
    total_earnings
HAVING
    total_earnings = MAX(total_earnings)
ORDER BY
    total_earnings DESC
LIMIT 1

