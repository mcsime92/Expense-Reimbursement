from random import randint

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

    # TODO: Increment employee ID


new_entry = NewEntry()
new_entry.summary_entry()  # This trigger the whole NewEntry class.


def additional_entry():
    if answer == 'Y':
        new_entry.summary_entry()

    elif answer == 'N':
        print('Done with employee management.')
    else:
        print('Please answer by Y or N')


# TODO: Delete employee
# TODO: Update employee

answer = input('Would you like to add more entries ? Y or N ')
additional_entry()

print(employee_list)

print('bye')
