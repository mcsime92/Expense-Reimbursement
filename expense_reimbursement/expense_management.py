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
        answer = input('What would you lke to do? Type 1, 2, or 3:\n'
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
        answer2 = input('What would you lke to do? Type 1, 2, or 3:\n'
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
    sql_command = """CREATE TABLE IF NOT EXISTS expenses (
                    first_name,
                    last_name,
                    description VARCHAR(40),
                    amount INTEGER);"""
    cursor.execute(sql_command)


# Testing only
def add_dummies():
    sql_command = """INSERT INTO expenses VALUES("Moe", "Sizlak", "Paper and pencils", 102.5);"""
    cursor.execute(sql_command)

    sql_command = """INSERT INTO expenses VALUES("Marge", "Simpson", "Glasses", 90);"""
    cursor.execute(sql_command)
    connection.commit()


def new_entry():
    input_first_name = input('> Employee first name ')
    input_last_name = input('> Employee last name ')
    input_description = input('> Expense description ')
    input_amount = input('> Amount ')

    sql_command = """INSERT INTO expenses VALUES (?, ?, ?, ?);"""
    cursor.execute(sql_command, (input_first_name, input_last_name, input_description, input_amount))
    connection.commit()


def delete_entry():
    search_last_name = input('> Provide employee last name of entry to be deleted: ')
    sql_command = """SELECT
                            first_name, last_name, description, amount 
                        FROM
                            expenses
                        WHERE
                            last_name = ?;"""
    cursor.execute(sql_command, (search_last_name,))

    ans = cursor.fetchmany(size=10)

    print("\nThese are the current entries:", ans)
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
    sql_command = """DELETE FROM expenses;"""
    cursor.execute(sql_command)
    connection.commit()


def drop_table():
    sql_command = """DROP TABLE expenses;"""
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
    cursor.execute("SELECT * FROM expenses")
    ans = cursor.fetchall()
    for i in ans:
        print(i)


# TODO: Protect from code injection for drop table etc.

connection = sqlite3.connect('employee_list.db')
cursor = connection.cursor()
database_creation()
print('\n>>> Expenses Management Interface <<<\n')

# add_dummies()

# print_db()

# functionality_choice()
print_db()

connection.close()

# Upcoming Structure - High Level
# TODO: 1 Expense report
# TODO: 1.01 Increment entry_id, starting from 1.

# TODO: 2 New table, join 2 tables: expense report to employee mgt
# TODO: 3 Generate basic report based on above table
# TODO: 4 Generate report with visuals based on above table
