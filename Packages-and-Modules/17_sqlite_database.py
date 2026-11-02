import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()
cursor.execute("CREATE TABLE students (name TEXT, marks INTEGER)")
cursor.execute("INSERT INTO students VALUES (?, ?)", ("Asha", 88))
cursor.execute("INSERT INTO students VALUES (?, ?)", ("Ravi", 76))
connection.commit()

for row in cursor.execute("SELECT name, marks FROM students"):
    print(row)

connection.close()
