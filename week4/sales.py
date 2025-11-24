# code for analysing the data from db 

import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="sales_cli"
)

df = pd.read_sql("SELECT * FROM sales", conn)
conn.close()

# simple analytics
df['revenue'] = df['quantity'] * df['price']
print("total revenue:", df['revenue'].sum())
print("best selling product:\n", df.groupby('product')['quantity'].sum())
