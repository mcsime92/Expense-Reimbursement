import sqlite3
from random import randint

connection = sqlite3.connect('employee_list.db')
cursor = connection.cursor()


def database_creation():
    sql_command = """CREATE TABLE IF NOT EXISTS emp (
                    id INTEGER PRIMARY KEY,
                    first_name,
                    last_name);"""

    cursor.execute(sql_command)


# Testing only
def add_dummies():
    sql_command = """INSERT INTO emp VALUES(343, "Moe", "Sizlak");"""
    cursor.execute(sql_command)

    sql_command = """INSERT INTO emp VALUES(453, "Marge", "Simpson");"""
    cursor.execute(sql_command)

    connection.commit()
    connection.close()


def new_entry():
    input_first_name = input('> Employee first name ')
    input_last_name = input('> Employee last name ')
    employee_id = randint(1, 1000)

    sql_command = """INSERT INTO emp VALUES (?, ?, ?);"""
    cursor.execute(sql_command, (employee_id, input_first_name, input_last_name))
    connection.commit()


def update_entry():
    search_last_name = input('> Provide employee last name to be updated: ')
    sql_command = """SELECT
                        id, first_name, last_name
                    FROM
                        emp
                    WHERE
                        last_name = ?;"""

    cursor.execute(sql_command, (search_last_name,))
    ans = cursor.fetchone()
    print("\nThis is the current entry:", ans, ".")
    choice = input("Press 1 to update first name, 2 to update last name: ")

    if choice == '1':
        first_name = input('Updated first name: ')
        sql_command = """UPDATE emp
                    SET
                        first_name = ?
                    WHERE
                        last_name = ?;"""
        cursor.execute(sql_command, (first_name, search_last_name))
        connection.commit()

    elif choice == '2':
        last_name = input('Updated last name: ')
        sql_command = """UPDATE emp
                            SET
                                last_name = ?
                            WHERE
                                last_name = ?;"""
        cursor.execute(sql_command, (last_name, search_last_name))
        connection.commit()

    else:
        print("ERROR: you pressed something else. Please try again.\n")
        update_entry()


def print_db():
    cursor.execute("SELECT * FROM emp")
    ans = cursor.fetchall()
    for i in ans:
        print(i)


database_creation()
# new_entry()
# update_entry()

print_db()
connection.close()
