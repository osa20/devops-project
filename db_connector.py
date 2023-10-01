import pymysql
import time

time.sleep(180)

schema_name = "mydb"


def create_table():
    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()
    # cursor.execute("GRANT ALL ON *.* TO 'c'@'%'")
    # cursor.execute("FLUSH PRIVILEGES")

    cursor.execute("DROP TABLE IF EXISTS mydb.users")

    # Inserting data into table
    statementToExecute = "CREATE TABLE IF NOT EXISTS `" + schema_name + "`.`users` (`user_id` INT NOT NULL, `user_name` VARCHAR(50) NOT NULL,`creation_date` DATE, PRIMARY KEY (`user_id`));"

    cursor.execute(statementToExecute)

    # cursor.execute("DROP TABLE mydb.users")
    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_table()


#############################

def add_user(user_id, user_name, creation_date):
    # Defining  my database
    # schema_name = "mydb"

    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # cursor.execute("GRANT ALL ON *.* TO 'c'@'%'")
    # cursor.execute("FLUSH PRIVILEGES")

    # Inserting user data into all the columns on database table
    cursor.execute(
        f"INSERT into mydb.users (user_id, user_name, creation_date) VALUES ({user_id}, '{user_name}', '{creation_date}')")

    cursor.close()
    conn.close()


if __name__ == '__main__':
    add_user(1, "Tom", "2023-08-20")
    add_user(2, "James", "2023-09-27")
    add_user(3, "David", "2023-09-28")
    add_user(4, "Greg", "2023-09-29")
    add_user(5, "Harry", "2023-09-30")
    add_user(6, "Jane", "2023-09-30")
    add_user(7, "Ricky", "2023-09-30")
