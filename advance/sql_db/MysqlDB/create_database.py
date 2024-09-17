from .dbConnection import cursor

def create_db():
    database_name = input("Enter a database name: ")
    Query = f'create database {database_name}'
    cursor.execute(Query)