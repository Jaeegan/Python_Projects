# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 18:12:00 2023

@author: Joshua
"""

import sqlite3

import pandas as pd

# sqlite3.Connection cannot be used with relative paths like ~/
conn = sqlite3.Connection("/Users/JG/Developer/Data/ShopeeInterview.db")

shopee_df = pd.read_excel(
    "~/Developer/Data/shopee_sample.xlsx", sheet_name=["Orders", "Customer"]
)

orders = shopee_df.get("Orders")
customers = shopee_df.get("Customer")

# Write data as tables to DataBase (connection)
orders.to_sql("Orders", con=conn, index=False)
customers.to_sql("Customer", con=conn, index=False)

c = conn.cursor()

# Qns: Count the number of customers per city
c.execute(
    """
          SELECT city, COUNT(DISTINCT 'Customer ID') AS num_of_customers
          FROM Customer
          GROUP BY city
          """
).fetchall()

# Qns: Count the number of orders per city
c.execute(
    """
          SELECT city, COUNT('Order ID') AS num_of_orders
          FROM Orders AS o
          LEFT JOIN Customer AS c
            ON c.'Customer ID' = o.'Customer ID'
          GROUP BY city
          """
).fetchall()

# Qns: Find the first order date of each customer
c.execute(
    """
          SELECT "Customer ID", MIN("Order Date") AS first_order_date
          FROM Orders
          GROUP BY "Customer ID"
          """
).fetchall()

# Qns: Find the number of customer who made their first order in each city, each day
c.execute(
    """
          SELECT city, first_order_date, COUNT("f.Customer ID") AS num_of_customers
          FROM (SELECT "Customer ID", MIN("Order Date") AS first_order_date
                FROM Orders
                GROUP BY "Customer ID") AS f
          LEFT JOIN Customer AS c
            ON f."Customer ID" = c."Customer ID"
          GROUP BY city, first_order_date
          """
).fetchall()

# Qns: Find the first order GMV (Sales) of each customer. If there is a tie, use the order with the lower order_id
c.execute(
    """
          SELECT 
              "Customer ID", 
              ROUND(SUM(Sales)/ COUNT("Order ID"), 2) AS GMV
          FROM Orders
          WHERE ("Customer ID", "Order Date") IN (
              SELECT "Customer ID", MIN("Order Date") first_date
              FROM Orders
              GROUP BY "Customer ID")
          GROUP BY "Customer ID"
          """
).fetchall()

# SELECT "Customer ID", Sales
# FROM Orders
# WHERE ("Customer ID", "Order Date") IN (
#     SELECT "Customer ID", MIN("Order Date") first_date
#     FROM Orders
#     GROUP BY "Customer ID")
