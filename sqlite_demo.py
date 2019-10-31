import sqlite3
from student import Student

conn = sqlite3.connect(':memory:')

my_cursor = conn.cursor()

my_cursor.execute("""CREATE TABLE student (
            firstname text,
            lastname text,
            rollnum integer
            )""")


def insert_student(student):
    print("inserting : {}".format(student.firstname))
    with conn:
        my_cursor.execute("INSERT INTO student VALUES (:firstname, :lastname, :rollnum)", {'firstname': student.firstname, 'lastname': student.lastname, 'rollnum': student.rollnum})

def get_all_students():
    print("List of students")
    my_cursor.execute("SELECT * FROM student")
    return my_cursor.fetchall()

def get_students_by_rollnum(rollnum):
    print("Get student for roll num : {}".format(rollnum))
    my_cursor.execute("SELECT * FROM student WHERE rollnum = :rollnum", {'rollnum': rollnum})
    return my_cursor.fetchall()


def update_student(firstname,lastname, rollnum):
    print("Update student with roll num : {}".format(rollnum))
    with conn:
        my_cursor.execute("UPDATE student SET firstname = :firstname , lastname = :lastname WHERE rollnum = :rollnum",
                  {'firstname': firstname, 'lastname':lastname, 'rollnum': rollnum})


def remove_student(student):
    print("Removing student : {}".format(student.firstname))
    with conn:
        my_cursor.execute("DELETE from student WHERE rollnum = :rollnum",
                  {'rollnum': student.rollnum})

student_1 = Student('Tejprakash', 'Kumawat', 12)
student_2 = Student('Ved', 'Kumawat', 9)
stars = "==============================================="
insert_student(student_1)
insert_student(student_2)
print(stars)

students = get_all_students()
print(students)
print(stars)
students = get_students_by_rollnum('12')
print(students)
print(stars)
update_student('Prakash','Pathak', 9)
print(stars)
students = get_all_students()
print(students)
print(stars)
remove_student(student_1)
print(stars)
students = get_all_students()
print(students)

conn.close()
