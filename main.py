import sqlite3
import pandas as pd

# STEP 1
conn = sqlite3.connect("data.sqlite")

# STEP 2
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName 
    FROM employees
""", conn)

# STEP 3
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber 
    FROM employees
""", conn)

# STEP 4
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""", conn)

# STEP 5
df_executive = pd.read_sql("""
    SELECT *,
        CASE 
            WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)

# STEP 6
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length 
    FROM employees
""", conn)

# STEP 7
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
    FROM employees
""", conn)

# STEP 8
# Use pd.read_sql to select priceEach * quantityOrdered, then use pandas .sum()
df_total = pd.read_sql("""
    SELECT priceEach * quantityOrdered AS total 
    FROM orderDetails
""", conn)
sum_total_price = df_total["total"].round().sum()

# STEP 9
# Keep STRFTIME outputs as string formatted padded dates ('06', '08', etc.)
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
           STRFTIME('%d', orderDate) AS day,
           STRFTIME('%m', orderDate) AS month,
           STRFTIME('%Y', orderDate) AS year
    FROM orders
""", conn)
