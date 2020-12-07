-- Solution to [Top Earners](https://www.hackerrank.com/challenges/earnings-of-employees/problem)

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
;
