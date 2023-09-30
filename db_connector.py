import pymysql


# '172.21.0.1'
# Creating table
def create_table():
    schema_name = "mydb"

    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    cursor.execute("GRANT ALL ON *.* TO 'c'@'%'")
    cursor.execute("FLUSH PRIVILEGES")

    # Deleting a table if it exists
    statementToExecute = "DROP TABLE  `" + schema_name + "`.`users`"
    cursor.execute(statementToExecute)
    # cursor.execute("DROP TABLE mydb.users")

    # Inserting data into table
    statementToExecute = "CREATE TABLE IF NOT EXISTS `" + schema_name + "`.`users` (`user_id` INT NOT NULL, `user_name` VARCHAR(50) " \
                                                                        "NOT NULL,`creation_date` DATE, PRIMARY KEY (`user_id`));"
    cursor.execute(statementToExecute)

    cursor.close()
    conn.close()


if __name__ == '__main__':
    create_table()


def add_user(user_id, user_name, creation_date):
    # Defining  my database
    schema_name = "mydb"

    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='user', passwd='password', db=schema_name,
                           database='mysql', local_infile=True)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    cursor.execute("GRANT ALL ON *.* TO 'c'@'%'")
    cursor.execute("FLUSH PRIVILEGES")

    # Inserting data into table
    statementToExecute = "CREATE TABLE `" + schema_name + "`.`users` (`user_id` INT NOT NULL, `user_name` VARCHAR(50) " \
                                                          "NOT NULL,`creation_date` DATE, PRIMARY KEY (`user_id`));"
    cursor.execute(statementToExecute)

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
