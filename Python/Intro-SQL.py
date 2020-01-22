import sqlite3

connection = sqlite3.connect('student.db') # file name
print("Database opened successfully.")

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")

print("table created successfully.")

## insert new record
# connection.execute("INSERT INTO " + TABLE_NAME + " VALUES ( 4, 'Pramod', 'DIT', 'Dehradun, Uttrakhand', 9810821705 ); " )
connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                   STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                    STUDENT_PHONE + " ) VALUES ( 'Gurjas', 'DIT', "
                                    "'Kapurthala, Punjab', 9810821705 ); ")
connection.commit()

## Dynamically adding values to database
for i in range(2):

    name = input('Enter your name')
    college = input('Enter your college')
    address = input('Enter your address')
    phone = input('Enter your phone number')

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " +
                      STUDENT_NAME + ", " +
                      STUDENT_COLLEGE + ", " + STUDENT_ADDRESS +
                      ", " + STUDENT_PHONE +
                      " ) VALUES ( '"+name+"', '"+college+"', " +
                       "'"+address+"', "+phone+" ); ")
    connection.commit()

## retrieve record
cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")

for row in cursor:
    print("Student id is: ", row[0])
    print("Student name is: ", row[1])
    print("Student college is: ", row[2])

connection.close()
