-- query_8.sql: Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT AVG(grades.grade)
FROM grades
JOIN subjects ON grades.subject_id = subjects.subject_id
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
WHERE teachers.name = 'Ruth Carlson';
