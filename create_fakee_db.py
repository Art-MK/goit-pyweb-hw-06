from faker import Faker
import sqlite3
import random

fake = Faker()

# Підключення до бази даних та створення курсора
conn = sqlite3.connect('university.db')
c = conn.cursor()

# Створення таблиць
c.execute('''CREATE TABLE students (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                group_id INTEGER)''')

c.execute('''CREATE TABLE groups (
                group_id INTEGER PRIMARY KEY,
                name TEXT)''')

c.execute('''CREATE TABLE teachers (
                teacher_id INTEGER PRIMARY KEY,
                name TEXT)''')

c.execute('''CREATE TABLE subjects (
                subject_id INTEGER PRIMARY KEY,
                name TEXT,
                teacher_id INTEGER)''')

c.execute('''CREATE TABLE grades (
                grade_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject_id INTEGER,
                grade INTEGER,
                date TEXT)''')

# Наповнення таблиць даними
groups = [(1, 'Group A'), (2, 'Group B'), (3, 'Group C')]
c.executemany('INSERT INTO groups VALUES (?, ?)', groups)

teachers = [(1, fake.name()), (2, fake.name()), (3, fake.name())]
c.executemany('INSERT INTO teachers VALUES (?, ?)', teachers)

subjects = [(1, 'Math', 1), (2, 'Physics', 2), (3, 'Chemistry', 3),
            (4, 'History', 1), (5, 'Literature', 2), (6, 'Biology', 3),
            (7, 'Geography', 1), (8, 'Foreign Language', 2)]
c.executemany('INSERT INTO subjects VALUES (?, ?, ?)', subjects)

students = []
for i in range(30):
    students.append((i+1, fake.name(), random.randint(1, 3)))
c.executemany('INSERT INTO students VALUES (?, ?, ?)', students)

grades = []
for student_id in range(1, 31):
    for subject_id in range(1, 4):
        for _ in range(random.randint(5, 10)):
            grade = random.randint(1, 100)
            date = fake.date_between(start_date='-1y', end_date='today')
            grades.append((student_id, subject_id, grade, date))
c.executemany('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', grades)

# Збереження змін та закриття підключення до бази даних
conn.commit()
conn.close()
