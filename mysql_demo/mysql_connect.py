import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="wowangle123"
)

my_cursor = my_db.cursor()

my_cursor.execute("CREATE DATABASE mydatabase")