# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:35:00 2021

@author: Joshua
"""

import sqlite3
import pandas as pd

#%%

# Create a connection
conn = sqlite3.Connection("C:/Users/Joseph/Python WD/Personal/output/university.db")

#%%

# Load CSV files into DataFrame
student = pd.read_csv("~/Joshua PFDS/ST2195 Course Files/Block 3/student.csv")
course = pd.read_csv("~/Joshua PFDS/ST2195 Course Files/Block 3/course.csv")
grade = pd.read_csv("~/Joshua PFDS/ST2195 Course Files/Block 3/grade.csv")

#%%

# Write record as tables to Database (connection)
student.to_sql('Student', con = conn, index = False) 
course.to_sql('Course', con = conn, index = False)
grade.to_sql('Grade', con = conn, index = False)

#%%

# Create cursor object c
# Concept of cursor is pretty abstract
# at current level of knowledge
# a cursor is reqiured to fetch and write commands
c = conn.cursor()

# Execute SQL commands using the function execute() and fetchall()
# Syntax below displays the tables within the database connection
c.execute('''
          SELECT name
          FROM sqlite_master
          WHERE type = "table"
          ''').fetchall()

#%%

# To view the Student table form the Database
# Extracted the data from the Database and create an alias
Student = c.execute("SELECT * FROM Student").fetchall()

# Since extracted data is of type 'list', use pandas to view as DataFrame
pd.DataFrame(Student)

#%%

# c.execute('''
#          CREATE TABLE Teacher (
#              staff_id TEXT PRIMARY KEY,
#              name TEXT)
#          ''')
          
#c.execute('''
#          DROP TABLE Teacher
#          ''')
          
#conn.commit()

#%%

# Appending a new row of observation
c.execute('''
          INSERT INTO Student
          VALUES (202029744, "Harper Taylor", 1)
          ''')
          
# Updating data
c.execute('''
          UPDATE Student
          SET student_id = "201929744"
          WHERE name = "Harper Taylor"
          ''')

#%%

# Deleting observation
c.execute('''
          DELETE FROM Student
          WHERE name = "Harper Taylor"
          ''')         
          
conn.commit()
conn.close()

#%%

# Query Databases in Python
# query 1 = q1
q1 = c.execute('''
               SELECT Student.name, final_mark
               FROM Student NATURAL JOIN Grade
               WHERE course_id = "ST101" 
               ORDER BY Student.name
               ''').fetchall()
               
pd.DataFrame(q1)

#%%

q2 = c.execute('''
               SELECT DISTINCT Course.name
               FROM (Student NATURAL JOIN Grade) JOIN Course USING (course_id)
               WHERE (Student.name = "Ava Smith" or Student.name = "Freddie Harris")
               ''').fetchall()
               
pd.DataFrame(q2)

#%%

q3 = c.execute('''
               SELECT course_id, ROUND(AVG(final_mark),3) as avg_mark
               FROM Grade
               GROUP BY course_id
               ''').fetchall()
               
pd.DataFrame(q3)
