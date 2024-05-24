-- query_5.sql: Знайти які курси читає певний викладач.
SELECT subjects.name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
WHERE teachers.name = 'Sarah Hutchinson';
