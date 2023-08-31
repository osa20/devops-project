import pymysql


def add_user(user_id, user_name, creation_date):
    # Defining  my database
    schema_name = "mydb"

    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting user data into table
    cursor.execute(
        f"INSERT into {schema_name}.users (user_id, user_name, creation_date) VALUES ({user_id}, '{user_name}', '{creation_date}')")

    cursor.close()
    conn.close()