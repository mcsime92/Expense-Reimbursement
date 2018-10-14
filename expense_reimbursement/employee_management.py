from random import randint
import pandas as pd

employee_list = []


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

        print(first_name, last_name, '- Employee ID:', employee_id)

        new_employee_entry = (employee_id, first_name, last_name)
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


# TODO: Increment employee ID or add a check to prevent duplicates

# TODO 3: Delete employee
# TODO 4: Update employee

# TODO 1: Check if CSV exists. If not, created in the end.

new_entry = NewEntry()
new_entry.summary_entry()  # This trigger the whole NewEntry class.

#print(employee_list) // for testing

#Saves the data to a csv file
df = pd.DataFrame(employee_list, columns=["EmployeeID", "FirstName", "LastName"])
df.to_csv('employee_list2.csv', sep=',', index=False)