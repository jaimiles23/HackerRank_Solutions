/**
     Solution to higher than 75 marks:
     https://www.hackerrank.com/challenges/more-than-75-marks/problem

     NOTES:
     - Write out the requirements for each query
     - MySQL has RIGHT() to get substring

Requirements:
- Student names
- marks higher than 75
- Order by last 3 characters of each name
- 2nd order by ID, ascending
*/

SELECT
    Name
FROM
    STUDENTS
WHERE
    Marks > 75
ORDER BY
    RIGHT(Name, 3),
    ID
    