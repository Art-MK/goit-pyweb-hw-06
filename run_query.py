import sqlite3
import os

# Підключення до бази даних
conn = sqlite3.connect('university.db')
c = conn.cursor()

# Функція для виконання SQL-запитів з файлу та виведення результатів
def execute_query(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sql_query = file.read()
    first_line = sql_query.splitlines()[0]
    print("\n" + "="*50)
    print(f"Запит з файлу {file_path}: {first_line}")
    c.execute(sql_query)
    results = c.fetchall()
    print("Результат:")
    for row in results:
        print(row)

# Отримання списку файлів SQL в поточній директорії
sql_files = [file for file in os.listdir() if file.endswith('.sql')]

# Виконання SQL-запитів для кожного файла
for file_path in sql_files:
    execute_query(file_path)

# Закриття підключення до бази даних
conn.close()
