'''
id INTEGER PRIMARY KEY AUTOINCREMENT,
product TEXT NOT NULL,
quantity INTEGER NOT NULL,
price REAL NOT NULL,
date TEXT NOT NULL
###
'''
import sqlite3
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM sales WHERE product = 'Laptop'")
rows= cursor.fetchall()
print("a")
for row in rows:
    print(row)

print("b")
cursor.execute("SELECT * FROM sales WHERE (date LIKE '2025-05-07' OR date LIKE '2025-05-08')")
rows= cursor.fetchall()
for row in rows:
    print(row)

print("c")
cursor.execute("SELECT * FROM sales WHERE price > 200")
rows= cursor.fetchall()
for row in rows:
    print(row)

print("d")
cursor.execute("SELECT product, SUM(price * quantity) AS total_sales \
               FROM sales GROUP BY product")
rows= cursor.fetchall()
for row in rows:
    print(row)

print("e")
cursor.execute("SELECT date, SUM(price * quantity) AS total_sales_day \
           FROM sales GROUP BY date ORDER BY total_sales_day desc LIMIT 1")
rows= cursor.fetchall()
for row in rows:
    print(row)
conn.close()


