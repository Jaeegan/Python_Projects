library(DBI)
library(dplyr)

# Create a connection
conn <- dbConnect(RSQLite::SQLite(), "~/..//R WD/Personal/output/university.db")
dbListTables(conn)

# Load CSV files into data.frame
student <- read.csv("~/..//Joshua PFDS/ST2195 Course Files/Block 3/student.csv", header = TRUE)
course <- read.csv("~/../Joshua PFDS/ST2195 Course Files/Block 3/course.csv", header = TRUE)
grade <- read.csv("~/..//Joshua PFDS/ST2195 Course Files/Block 3/grade.csv", header = TRUE)

# Write record as tables to Database (connection)
dbWriteTable(conn, "Student", student)
dbWriteTable(conn, "Course", course)
dbWriteTable(conn, "Grade", grade)

dbListTables(conn)

# To view the Student table from the Database
dbReadTable(conn, "Student")

# Make reference to a table in the Database
# This allow us to know the type of data recorded in each attributes
tbl(conn, "Student")

###############################################################################################

# Execcute SQL commands using the function dbExecute() or db<specific command>()

# dbCreateTable(conn, "Teacher", c(staff_id = "TEXT", name = "TEXT"))

# dbExecute(conn,
#        "CREATE TABLE Teacher (
#               staff_id TEXT PRIMARY KEY,
#               name TEXT)")

# dbExecute(conn,
#        "DROP TABLE Teacher")

# dbRemoveTable(conn, "Teacher")

###############################################################################################

# Appending a new row of observation

# dbExecute(conn,
#         "INSERT INTO Student VALUES (202029744, 'Harper Taylor', 1)")

dbAppendTable(conn, "student", data.frame(student_id = "202029744", 
                                          name = "Harper Taylor", 
                                          year = 1))

# Updating data
dbExecute(conn,
          "UPDATE Student
          SET student_id='201929744'
          WHERE name='Harper Taylor'")

# Deleting observation
dbExecute(conn,
          "DELETE FROM Student
          WHERE name = 'Harper Taylor'")

dbReadTable(conn, "student")

# Deleting specific observation with 2 criteria
dbExecute(conn, 
          "DELETE FROM Grade
          WHERE student_id='201933222'
          AND course_id='ST207'")

dbReadTable(conn, "Grade")

dbExecute(conn, 
          "INSERT INTO Grade
          VALUES ('ST207', 201933222, 73)")


###############################################################################################

# Query Databases in R
# query 1 = q1

q1 <- dbGetQuery(conn,
                "SELECT Student.name, final_mark
                FROM student, Grade
                WHERE Grade.course_id = 'ST101'
                AND Student.student_id = Grade.student_id")
print(q1)


q2 <- dbGetQuery(conn,
                 "SELECT DISTINCT Course.name
                 FROM Student, Grade, Course
                 WHERE (Student.name = 'Ava Smith' or Student.name = 'Freddie Harris')
                 AND Student.student_id = Grade.student_id
                 AND Grade.course_id = Course.course_id")
print(q2)

# Alternate syntax for sending query
# dbFetch() function extracts query result to R as data.frame
# When dealing with large table, this method may be more useful to read data
# For instance, dbFetch(query, n = 10), fetches the first batch of 10 observations
q3 <- dbSendQuery(conn, 
                  "SELECT Student.name, final_mark
                  FROM Student NATURAL JOIN Grade
                  WHERE Grade.course_id = 'ST101'")
print(q3)

# While loop returns batches of result till dbHasCompleted = TRUE
while (!dbHasCompleted(q3)) {
  df <- dbFetch(q3, n = 1)
  print(df)
}

dbFetch(q3, n = 1)
dbFetch(q3, n = 1)

# Check the status of a query
dbHasCompleted(q3)

dbFetch(q3, n = 1)
dbHasCompleted(q3)

dbGetInfo(q3)

# Free all results from the query
dbClearResult(q3)

q3 <- dbSendQuery(conn, 
                  "SELECT Student.name, final_mark
                  FROM Student NATURAL JOIN Grade
                  WHERE Grade.course_id = 'ST101'") %>% dbFetch()
print(q3)

# Indicates data type as "data.frame"
class(q3)
###############################################################################################

# Query database using dplyr package
# Create alias (reference) for tables from conn to manipulate in R
student_db <- tbl(conn, "Student")
grade_db <- tbl(conn, "Grade")
course_db <- tbl(conn, "Course")

q4 <- inner_join(student_db, grade_db) %>% 
  filter(course_id == "ST101", student_id) %>% 
  select(name, final_mark)

print(q4)

show_query(q4)

# | operator represents OR
q5 <- inner_join(student_db, grade_db, by = c("student_id" = "student_id")) %>% 
  inner_join(course_db, by = "course_id", suffix = c(".student", ".course")) %>% 
  filter(name.student == "Ava Smith" | name.student == "Freddie Harris") %>% 
  select(name.course) %>% 
  distinct()
                 
print(q5)

# Summarise() function creates a new data.frame
# The rounded average of final_mark(s) are assigned to a new variable called avg_mark
# na.rm represents NOT AVAILABLE REMOVE, which is set to TRUE to omit values that are
# not int to prevent the code from breaking
q6 <- grade_db %>% 
  group_by(course_id) %>% 
  summarise(avg_mark = round(mean(final_mark, na.rm = TRUE), 1))

print(q6)

dbDisconnect(conn)

