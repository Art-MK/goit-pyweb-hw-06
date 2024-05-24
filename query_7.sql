-- query_7.sql: Знайти оцінки студентів у окремій групі з певного предмета.
SELECT students.name, grades.grade
FROM students
JOIN groups ON students.group_id = groups.group_id
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE groups.name = 'Group C' AND subjects.name = 'Math';
