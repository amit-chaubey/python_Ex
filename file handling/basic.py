###Q1
with open('file handling/notes.txt', 'w') as file:
    file.write("Hello, This is a test file")

###Q2
try:
    with open('file handling/notes.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found")

###Q3

try:
    with open('file handling/notes.txt', 'a') as file:
        file.write('\nThis is new line.')
    print("File updated successfully")
except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print(f"Error: {e}")

###Q4

try:
    with open('file handling/notes.txt', 'r') as file:
        for idx, line in enumerate(file, start = 1):
            print(f"{idx}, {line}")
except FileNotFoundError:
    print("Error: File not found")

###Q5

try:
    with open('file handling/notes.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print(f"Error: {e}")
except PermissionError:
    print("Error: Permission denied")


###Q6

def read_file(file_path):
    """Reads a file and returns the content"""
    try:
        with open(file_path, 'r') as file:
            print("file content:\n" + file.read())
    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print(f"Error: {e}")

read_file('file handling/notes.txt')

###Q7

import os
import shutil

def safe_write(file_path, content):
    """Safely writes content to a file, creating backup if file exists"""
    try:
        if os.path.exists(file_path):
            backup_file = file_path + '.bak'
            shutil.copy(file_path , backup_file)
            print(f"Backup file created: {backup_file}")

        with open(file_path, "w") as file:
            file.write(content)
        print(f"File {file_path} written successfully")
    except FileNotFoundError:
        print(f"Error: File not found")
    except Exception as e:
        print(f"Error: {e}")

safe_write('file handling/new-notes.txt', "This is a new version of the file.")

###Q8

import csv

students = [
    {"name": "John", "age": 20, "grade": 85},
    {"name": "Jane", "age": 21, "grade": 90},
    {"name": "Jim", "age": 22, "grade": 88},
]


try:
    with open('file handling/students.csv', 'w',  newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "grade"])
        writer.writeheader()
        writer.writerows(students)
    print("Student data saved successfully")
except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print(f"Error: {e}")

###Q9

import csv

with open('file handling/students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        print(f"Name: {row['name']}, Age: {row['age']}, Grade: {row['grade']}")