-- query_9.sql: Знайти список унікальних курсів, які відвідує студент.
SELECT DISTINCT subjects.name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
JOIN students ON grades.student_id = students.student_id
WHERE students.name = 'Barbara Davis';
