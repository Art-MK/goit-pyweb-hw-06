-- query_10.sql: Список курсів, які певний студент читає певний викладач.
SELECT DISTINCT subjects.name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
JOIN students ON grades.student_id = students.student_id
JOIN teachers ON subjects.teacher_id = teachers.teacher_id
WHERE students.name = 'Michelle Scott' AND teachers.name = 'Michael Caldwell';
