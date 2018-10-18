import sqlite3
import datetime


# Document number generator using current time
def document_number_gen():
    now = datetime.datetime.now()
    now_string = str(now)
    now_cleaned = ''.join(e for e in now_string if e.isalnum())
    now_cleaned_short = now_cleaned[:16]
    return now_cleaned_short


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
                    doc_number INTEGER,
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
    doc_number = document_number_gen()
    input_first_name = input('> Employee first name ')
    input_last_name = input('> Employee last name ')
    input_description = input('> Expense description ')
    input_amount = input('> Amount ')

    sql_command = """INSERT INTO expenses VALUES (?, ?, ?, ?, ?);"""
    cursor.execute(sql_command, (doc_number, input_first_name, input_last_name, input_description, input_amount))
    connection.commit()


# Requests user input, provides last name.
# Entries for last name are shown with ID of expense entry.
# User decides which entry to delete, or to cancel.

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

    print("\nThese are the current entries for your selection:", ans)
    choice = input("Which entry do you want to delete? Enter the entry ID provided above or type 'None to cancel: ")

    if isinstance(choice, int):
        sql_command = """DELETE
                            FROM
                                expenses
                            WHERE
                                ID = ?;"""
        cursor.execute(sql_command, (choice,))
        connection.commit()

    else:
        print('No entry were deleted.')
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
                        doc_number, first_name, last_name
                    FROM
                        expenses
                    WHERE
                        last_name = ?;"""

    cursor.execute(sql_command, (search_last_name,))
    ans = cursor.fetchmany(size=10)
    print("\nThese are the current entries:", ans, ".")
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

functionality_choice()

print_db()

connection.close()

# Upcoming Structure - High Level
# TODO: 1 Expense report
# TODO: 1.01 Increment entry_id, starting from 1.

# TODO: 2 New table, join 2 tables: expense report to employee mgt
# TODO: 3 Generate basic report based on above table
# TODO: 4 Generate report with visuals based on above table
