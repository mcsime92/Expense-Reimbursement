from random import randint
import pandas as pd
import csv
from pathlib import Path

employee_list = []
employee_db = 'employee_list.csv'


class DataManagement(object):
    def data_to_file(self):
        my_file = Path(employee_db)
        if my_file.is_file():
            with open(employee_db, 'a') as ed:
                for item in employee_list:
                    ed.write((",".join(map(str, item))))
                    ed.write("\n")
        else:
            df = pd.DataFrame(employee_list, columns=["EmployeeID", "FirstName", "LastName"])
            df.to_csv(employee_db, sep=',', index=False)

    def show_entry(self):
        my_file = Path(employee_db)
        if my_file.is_file():
            record = input('Enter employee ID, first or last name ')
            csv_file = csv.reader(open(employee_db, 'rt', encoding = 'utf-8'), delimiter=',')
            for row in csv_file:
                if record == row[0] or record == row[1] or record == row[2]:
                    print(row)


        else:
            print('There is no such file')

    def delete_entry(self):
        pass

    def update_entry(self):
        pass


class NewEntry(object):
    def gen_employee_name(self):
        input_first_name = input('> Employee first name ')
        input_last_name = input('> Employee last name ')
        return input_first_name, input_last_name

    def gen_employee_id(self):
        employee_id = randint(1, 1000)
        return employee_id

    def summary_entry(self):
        first_name, last_name = NewEntry().gen_employee_name()  # unpacking
        employee_id = NewEntry().gen_employee_id()

        new_employee_entry = employee_id, first_name, last_name
        employee_list.append(new_employee_entry)

        NewEntry().question()

    def question(self):
        answer = input('\nWould you like to add more entries ? Y or N ')

        if answer == 'Y':
            NewEntry().summary_entry()
        elif answer == 'N':
            print('\nDone with employee management.')
        else:
            print('Please answer by Y or N')
            NewEntry().question()
        return answer


class ManageEntry(object):
    def show_entry(self):
        pass

    def delete_entry(self):
        pass

    def update_entry(self):
        pass


manage_entry = ManageEntry()
new_entry = NewEntry()
data_management = DataManagement()


# TODO 1: Increment employee ID or add a check to prevent duplicates
# TODO 3: Delete employee
# TODO 4: Update employee
# TODO 5: Try catch for PermissionError: [Errno 13] Permission denied: 'employee_list.csv'
# TODO : Contextual menu: 1. New entry, 2. Manage entries, 3. Quit


def functionality_choice():
    functionality = input('What would you lke to do? Type 1, 2 or 3:\n'
                          '1. New entry\n'
                          '2. Manage entries\n'
                          '3. Quit\n')

    if functionality == "1":
        NewEntry().summary_entry()
    elif functionality == "2":
        DataManagement().show_entry()
    elif functionality == "3":
        print('Exit')
        exit()
    else:
        print('Please answer 1, 2 or 3')
        functionality_choice()


print('>>> Employee Management Interface <<<\n')
functionality_choice()

# print(employee_list) // for testing

# Checks if a file exists. If yes, uses it. If no, creates it with data.
