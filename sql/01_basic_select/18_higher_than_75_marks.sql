/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 11:48:48
 * @modify date 2020-09-05 11:48:48
 * @desc [
     Solution to higher than 75 marks:
     https://www.hackerrank.com/challenges/more-than-75-marks/problem

     NOTES:
     - Write out the requirements for each query
     - MySQL has RIGHT() to get substring
 ]
 */

/*
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
    