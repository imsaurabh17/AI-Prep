import sqlite3

conn = sqlite3.connect("my_database.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee_details(
               employee_id int primary key,
               firstname text not null,
               lastname text not null,
               department text not null,
               salary int,
               hire_date date,
               gender text
               )
""")


emplyee_data = [
    (101, 'John', 'Smith', 'Engineering', 95000, '2018-03-15', 'Male'),
    (102, 'Jane', 'Doe', 'Marketing', 78000, '2019-06-20', 'Female'),
    (103, 'Michael', 'Johnson', 'Sales', 85000, '2017-09-01', 'Male'),
    (104, 'Emily', 'Davis', 'Human Resources', 65000, '2020-01-10', 'Female'),
    (105, 'David', 'Wilson', 'Engineering', 110000, '2016-11-25', 'Male'),
    (106, 'Sarah', 'Miller', 'Finance', 90000, '2018-05-30', 'Female'),
    (107, 'Robert', 'Brown', 'IT', 120000, '2015-02-12', 'Male'),
    (108, 'Jessica', 'Garcia', 'Marketing', 82000, '2021-04-05', 'Female'),
    (109, 'Chris', 'Martinez', 'Sales', 88000, '2019-07-18', 'Male'),
    (110, 'Anna', 'Rodriguez', 'IT', 105000, '2017-10-22', 'Female')
]

# cursor.executemany("""
#     INSERT INTO employee_details(employee_id,firstname,lastname,department,salary,hire_date,gender) VALUES (?,?,?,?,?,?,?)   
# """,emplyee_data)

cursor.execute("""SELECT firstname,salary from employee_details where salary > (SELECT avg(salary) FROM employee_details) 
                    
               """)

for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()