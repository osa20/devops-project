import pymysql


# Creating a function for GET method
def get_user(user_id):
    schema_name = "mydb"
    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Extracting a user data from database table
    cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id = {user_id}")
    # This for-loop only retrieves the uer data for a single user...
    # as only a single use is being used here
    for row in cursor:
        return row


# Creating a function for POST method
def create_user(user_id, user_name, creation_date):
    schema_name = "mydb"
    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting user data into all the columns on database table
    return cursor.execute(
        f"INSERT into mydb.users (user_id, user_name, creation_date) VALUES ({user_id}, '{user_name}', '{creation_date}')")


# Creating a function for PUT method
def update_user(user_id, user_name):
    schema_name = "mydb"

    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # updating user data in database table
    return cursor.execute(f"UPDATE {schema_name}.users SET user_name = '{user_name}' WHERE user_id = {user_id}")


# Creating a function for DELETE method
def delete_user(user_id):
    schema_name = "mydb"

    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # deleting user data in database table
    return cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = {user_id}")