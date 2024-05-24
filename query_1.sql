-- query_1.sql: Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT students.name, AVG(grades.grade) as average_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
GROUP BY students.student_id
ORDER BY average_grade DESC
LIMIT 5;