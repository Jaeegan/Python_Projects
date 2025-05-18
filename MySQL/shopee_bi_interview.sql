
CREATE DATABASE shopee;

USE shopee;

-- SHOW GLOBAL VARIABLES LIKE 'local_infile';
-- SET global local_infile=TRUE;

CREATE TABLE IF NOT EXISTS shopee.Customers (
    customerid VARCHAR(255),
    customername VARCHAR(255),
    segment VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255)
);

LOAD DATA LOCAL INFILE "//Users//JG//Developer//Data//customers.csv" INTO TABLE shopee.Customers
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (customerid,customername,segment,city,state);

CREATE TABLE IF NOT EXISTS shopee.Orders (
    rowid INT,
    orderid VARCHAR(255),
    orderdate DATE,
    shipdate DATE,
    shipmode VARCHAR(255),
    customerid VARCHAR(255),
    country VARCHAR(255),
    postalcode TEXT,
    region VARCHAR(255),
    productid VARCHAR(255),
    category VARCHAR(255),
    subcategory VARCHAR(255),
    productname VARCHAR(255)
);

ALTER TABLE shopee.Orders 
    ADD sales FLOAT, 
    ADD quantity INT,
    ADD discount FLOAT,
    ADD profit FLOAT,
    ADD unknown FLOAT;

-- Replace texts containing ',' with ';' to prevent MySQL from mis-parsing the data
LOAD DATA LOCAL INFILE "//Users//JG//Developer//Data//orders.csv" INTO TABLE shopee.Orders
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (rowid,orderid,@orderdate,@shipdate,shipmode,customerid,country,postalcode,region,productid,category,subcategory,productname,sales,quantity,discount,profit,unknown)
    set orderdate=STR_TO_DATE(@orderdate, '%d/%m/%Y'), shipdate=STR_TO_DATE(@shipdate, '%d/%m/%Y');

-- ---------------------------------------------------------------------------------------------------------------------------------------------------

-- Number of customers per city:
SELECT 
	city, 
    COUNT(DISTINCT customerid) num_of_customers
FROM shopee.Customers
GROUP BY city;

-- Count the number of orders per city:
SELECT
	city, 
	COUNT(orderid) num_of_orders
FROM shopee.Orders o
LEFT JOIN shopee.Customers c
    ON o.customerid = c.customerid
GROUP BY city
ORDER BY city;