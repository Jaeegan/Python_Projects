
-- DROP DATABASE DB;
-- A server cannot be established without a database
-- To create a new database without connection:
CREATE DATABASE mac;

-- Establish connection to the database
-- Once that is done, refresh connections and check if database exists
USE mac;


CREATE TABLE IF NOT EXISTS mac.emp (
    deptno int,
    ename varchar(100),
    dept varchar(100),
    sal int,
    comm int
);

INSERT INTO mac.emp VALUES (1, 'John', 'HR', 4000, 0);
INSERT INTO mac.emp VALUES (2, 'Sally', 'Finance', 10000, 300);
INSERT INTO mac.emp VALUES (3, 'Amy', 'Sales', 3500, 2000);

SELECT * FROM mac.emp;

-- Clear table contents
DELETE FROM mac.emp

-- Import csv file to Table
LOAD DATA LOCAL INFILE 'filepath' INTO TABLE mac.emp
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    ()
