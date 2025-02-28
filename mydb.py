# Install mqsql on your computer
# pip install mysql                               for database
# pip install mysql-connector                     for connecting database to project
# pip install mysql-connector-python              for connecting database to project


import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '0*ALPITG*0'
)

# prepare a cursor object
cursorObject = database.cursor()

# create database

cursorObject.execute("CREATE DATABASE elderco")

print("All Done")

# run this in cmd by (python mydb.py) than run migrate by (python manage.py migrate)