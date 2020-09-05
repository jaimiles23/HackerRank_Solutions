/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-05 12:51:16
 * @modify date 2020-09-05 12:51:16
 * @desc [
    Solution to The Report:
    https://www.hackerrank.com/challenges/the-report/problem
 
 Requirements:
    - Columns: Name, Grade, Mark
    - If mark < 8, name = NULL
    - Order by: 
        - Grade desc
        - Name asc
    
NOTES:
    - Join on Marks using the BETWEEN operator
        - Let's you select a range between 2 columns.
    - IF statement can be used inside SELECT to determine pull.
 ]
 */



SELECT
    IF (Grades.Grade > 7, Students.Name, NULL),
    Grades.Grade,
    Students.Marks
FROM
    Students
INNER JOIN Grades
    ON Students.Marks BETWEEN Grades.Min_Mark AND Grades.Max_Mark
ORDER BY
    Grades.Grade DESC,
    Students.Name
    




