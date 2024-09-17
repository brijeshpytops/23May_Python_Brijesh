from .dbConnection import cursor

def read_data_from_table():
    # Query = "select * from users order by  last_name DESC limit 5"
    # cursor.execute(Query)
    # for record in  cursor.fetchall():
    #     print(record[1:3])


    Query = "select count(user_id) from users"
    cursor.execute(Query)
    result = cursor.fetchone()
    print(f"Total number of users: {result[0]}")