from .dbConnection import cursor

def create_tab():
    table_name = input("Enter a table name : ")
    columns = input("Enter columns configs : ")
    Query = f"create table {table_name} ({columns});"
    print(Query)
    cursor.execute(Query)