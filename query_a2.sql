-- query_11.sql: Середній бал, який певний викладач ставить певному студентові.
SELECT students.name AS student_name, AVG(grades.grade) AS average_grade
FROM students
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
WHERE teachers.name = 'Michael Caldwell' AND students.name = 'Michelle Scott'
GROUP BY students.name;
