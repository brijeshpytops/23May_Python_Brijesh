# pip install mysql-connector-python
import mysql.connector

db = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='facebook')

cursor = db.cursor()