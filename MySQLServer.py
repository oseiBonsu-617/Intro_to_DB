import mysql.connector

try:
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Nobbonsu617$",
        database = "alx_book_store"
)


    cursor = db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

    # Close connection
    cursor.close()
    db.close()
    
except mysql.connector.Error:
    print("Connection Failed")
