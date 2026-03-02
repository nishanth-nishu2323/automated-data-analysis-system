import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="automated_analysis"
    )
    print("Connection successful!")
except Exception as e:
    print("Error:", e)