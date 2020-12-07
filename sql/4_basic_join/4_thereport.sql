-- Solution to [The Report](https://www.hackerrank.com/challenges/the-report/problem)

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