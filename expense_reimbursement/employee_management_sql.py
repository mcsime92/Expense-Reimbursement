import sqlite3
from random import randint


def functionality_choice():
    functionality = input('What would you like to do? Type 1, 2, 3 or 4:\n'
                          '1. New entry \n'
                          '2. Manage entries \n'
                          '3. Manage table \n'
                          '4. Quit ')

    if functionality == "1":
        new_entry()

    elif functionality == "2":
        answer = input('What would you like to do? Type 1, 2, or 3:\n'
                       '1. Update entry \n'
                       '2. Delete entry \n'
                       '3. Quit ')

        if answer == "1":
            update_entry()
        elif answer == "2":
            delete_entry()
        elif answer == "3":
            print('Exit')
            exit()
        else:
            print('ERROR. Please answer 1, 2 or 3')
            functionality_choice()

    elif functionality == "3":
        answer2 = input('What would you like to do? Type 1, 2, or 3:\n'
                        '1. Delete table \n'
                        '2. Drop table \n'
                        '3. Quit ')

        if answer2 == "1":
            delete_table()
        elif answer2 == "2":
            drop_table()
        elif answer2 == "3":
            print('Exit')
            exit()
        else:
            print('ERROR. Please answer 1, 2 or 3')
            functionality_choice()

    elif functionality == "4":
        print('Exit')
        exit()
    else:
        print('Please answer 1, 2, 3 or 4')
        functionality_choice()


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

    sql_command = """INSERT INTO emp VALUES(454, "Lisa", "Simpson");"""
    cursor.execute(sql_command)

    sql_command = """INSERT INTO emp VALUES(455, "Bart", "Simpson");"""
    cursor.execute(sql_command)

    connection.commit()


def new_entry():
    input_first_name = input('> Employee first name ')
    input_last_name = input('> Employee last name ')
    employee_id = randint(1, 1000)

    sql_command = """INSERT INTO emp VALUES (?, ?, ?);"""
    cursor.execute(sql_command, (employee_id, input_first_name, input_last_name))
    connection.commit()

    answer = input('\nWould you like to add more entries ? Y or N ')

    if answer == 'Y':
        new_entry()
    elif answer == 'N':
        print('\nDone with new entries.')

    else:
        print('Please answer by Y or N\n')
        new_entry()


def delete_entry():
    search_last_name = input('> Provide employee last name to be deleted: ')
    sql_command = """SELECT
                            id, first_name, last_name
                        FROM
                            emp
                        WHERE
                            last_name = ?;"""

    cursor.execute(sql_command, (search_last_name,))

    ans = cursor.fetchone()

    print("\nThis is the current entry:", ans)
    choice = input("Do you want to delete this entry? Press Y to delete, N to cancel: ")

    if choice == 'Y':
        sql_command = """DELETE
                        FROM
                            emp
                        WHERE
                            last_name = ?;"""
        cursor.execute(sql_command, (search_last_name,))
        connection.commit()

    elif choice == 'N':
        print('No entry were deleted.')

    else:
        print("\nERROR: you pressed something else. Please try again.\n")
        delete_entry()


def delete_table():
    sql_command = """DELETE FROM emp;"""
    cursor.execute(sql_command)
    connection.commit()


def drop_table():
    sql_command = """DROP TABLE emp;"""
    cursor.execute(sql_command)
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
        print("\nERROR: you pressed something else. Please try again.\n")
        update_entry()


# Testing
def print_db():
    cursor.execute("SELECT * FROM emp")
    ans = cursor.fetchall()
    for i in ans:
        print(i)


# TODO: Protect from code injection for drop table etc.

connection = sqlite3.connect('employee_list.db')
cursor = connection.cursor()
database_creation()
print('\n>>> Employee Management Interface <<<\n')


functionality_choice()

connection.close()
