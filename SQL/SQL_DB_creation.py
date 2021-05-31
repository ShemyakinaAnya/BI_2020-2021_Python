import csv
import sqlite3


connection = sqlite3.connect('/home/haletod/PycharmProjects/Ligase/students_and_alcohol.db')
cursor = connection.cursor()


# create table with students info

(cursor.execute(
    "CREATE TABLE IF NOT EXISTS students_info (student_id INTEGER, sex TEXT, age INTEGER, famsize TEXT, Pstatus TEXT, "
    "failures INTEGER, health INTEGER, guardian TEXT, PRIMARY KEY(student_id));"))

with open('students.csv') as csv_data:
    data = csv.DictReader(csv_data)
    to_db = [
        (i['student_id'], i['sex'], i['age'], i['famsize'], i['Pstatus'], i['failures'], i['health'], i['guardian'])
        for i in data]

(cursor.executemany(
    "INSERT INTO students_info (student_id, sex, age, famsize, Pstatus, failures, health, guardian) "
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?);",
    to_db))


# create table with students alcohol consumption

(cursor.execute(
    "CREATE TABLE IF NOT EXISTS alcohol_consumption (student_id INTEGER, Daily INTEGER, Weekly INTEGER, "
    "PRIMARY KEY(student_id) FOREIGN KEY(student_id) REFERENCES students_info(student_id) ON DELETE CASCADE "
    "ON UPDATE CASCADE);"))

with open('students.csv') as csv_data:
    data = csv.DictReader(csv_data)
    to_db = [(i['student_id'], i['Dalc'], i['Walc']) for i in data]

cursor.executemany("INSERT INTO alcohol_consumption (student_id, Daily, Weekly) VALUES (?, ?, ?);", to_db)

connection.commit()
connection.close()
