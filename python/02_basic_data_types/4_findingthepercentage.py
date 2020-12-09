# Solution to [Finding the percentage](https://www.hackerrank.com/challenges/finding-the-percentage)

if __name__ == '__main__':
    def mean(marks: list) -> float:
        """Returns mean of student's marks formatted to 2 decimal places

        Args:
            marks (list): student's marks

        Returns:
            float: Average score
        """
        avg_mark = sum(marks) / len(marks)
        return f"{avg_mark:.2f}"    # 2 decimal places.


    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks.get(query_name, 0)
    print(mean(marks)) 