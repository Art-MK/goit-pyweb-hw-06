
from faker import Faker
import sqlite3
import random

fake = Faker()

# Підключення до бази даних та створення курсора
conn = sqlite3.connect('university.db')
c = conn.cursor()

# Створення таблиць з зовнішніми ключами
c.execute('''CREATE TABLE IF NOT EXISTS groups (
                group_id INTEGER PRIMARY KEY,
                name TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS teachers (
                teacher_id INTEGER PRIMARY KEY,
                name TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS subjects (
                subject_id INTEGER PRIMARY KEY,
                name TEXT,
                teacher_id INTEGER,
                FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                group_id INTEGER,
                FOREIGN KEY (group_id) REFERENCES groups(group_id))''')

c.execute('''CREATE TABLE IF NOT EXISTS grades (
                grade_id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject_id INTEGER,
                grade INTEGER,
                date TEXT,
                FOREIGN KEY (student_id) REFERENCES students(student_id),
                FOREIGN KEY (subject_id) REFERENCES subjects(subject_id))''')

# Наповнення таблиць даними
groups = [(1, 'Group A'), (2, 'Group B'), (3, 'Group C')]
c.executemany('INSERT INTO groups (group_id, name) VALUES (?, ?)', groups)

teachers = [(1, fake.name()), (2, fake.name()), (3, fake.name())]
c.executemany('INSERT INTO teachers (teacher_id, name) VALUES (?, ?)', teachers)

subjects = [(1, 'Math', 1), (2, 'Physics', 2), (3, 'Chemistry', 3),
            (4, 'History', 1), (5, 'Literature', 2), (6, 'Biology', 3),
            (7, 'Geography', 1), (8, 'Foreign Language', 2)]
c.executemany('INSERT INTO subjects (subject_id, name, teacher_id) VALUES (?, ?, ?)', subjects)

students = [(i, fake.name(), random.choice([1, 2, 3])) for i in range(1, 31)]
c.executemany('INSERT INTO students (student_id, name, group_id) VALUES (?, ?, ?)', students)

grades = [(i, random.randint(1, 30), random.randint(1, 3), random.randint(60, 100), fake.date()) for i in range(1, 101)]
c.executemany('INSERT INTO grades (grade_id, student_id, subject_id, grade, date) VALUES (?, ?, ?, ?, ?)', grades)

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()
