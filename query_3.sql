-- query_3.sql: Знайти середній бал у групах з певного предмета.
SELECT groups.name, AVG(grades.grade) as average_grade
FROM groups
JOIN students ON groups.group_id = students.group_id
JOIN grades ON students.student_id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.subject_id
WHERE subjects.name = 'Chemistry'
GROUP BY groups.group_id;
