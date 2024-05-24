-- query_12.sql: Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT students.name AS student_name, grades.grade
FROM students
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id
JOIN groups ON students.group_id = groups.group_id
WHERE groups.name = 'Group A' AND subjects.name = 'Physics' AND grades.date = (
    SELECT MAX(date)
    FROM grades
    JOIN subjects ON grades.subject_id = subjects.subject_id
    WHERE subjects.name = 'Physics' AND students.student_id = grades.student_id
);
