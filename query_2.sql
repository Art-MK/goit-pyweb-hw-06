-- query_2.sql: Знайти студента із найвищим середнім балом з певного предмета.
SELECT students.name
FROM students
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE subjects.name = 'Physics'
GROUP BY students.name
ORDER BY AVG(grades.grade) DESC
LIMIT 1;

