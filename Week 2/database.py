import sqlite3

conn = sqlite3.connect("my_database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               student_id int not null,
               student_name text not null,
               subject text not null,
               marks int not null,
               attendance text not null,
               department text not null
               )
""")


students = [
    (1,"Arjun","Math",78,90,"Science"),
    (2,"Sneha","Math",65,85,"Science"),
    (3,"Rahul","Physics",88,95,"Science"),
    (4,"Meera","History",92,80,"Arts"),
    (5,"Kiran","Math",55,70,"Science"),
    (6,"Ananya","History",81,88,"Arts"),
    (7,"Pranav","Physics",73,92,"Science"),
    (8,"Isha","Math",95,96,"Science"),
    (9,"Dev","History",60,85,"Arts"),
    (10,"Naina","Physics",84,90,"Science")
]

cursor.executemany("""
    INSERT INTO students (student_id,student_name,subject,marks,attendance,department) VALUES (?,?,?,?,?,?)
""",students)

cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()