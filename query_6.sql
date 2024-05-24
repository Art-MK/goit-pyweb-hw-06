-- query_6.sql: Знайти список студентів у певній групі.
SELECT students.name
FROM students
JOIN groups ON students.group_id = groups.group_id
WHERE groups.name = 'Group B';
