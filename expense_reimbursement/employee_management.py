from random import randint

employee_list = []

def gen_employee_name():
    input_first_name = input('> Employee first name ')
    input_last_name = input('> Employee last name ')
    return input_first_name, input_last_name


def gen_employee_id():
    employee_id = randint(1, 1000)
    return employee_id

#TODO: Increment employee ID

first_name, last_name = gen_employee_name() # unpacking
employee_id = gen_employee_id()

print(first_name, last_name, '- Employee ID:', employee_id)

new_entry = (employee_id, first_name, last_name)

employee_list.append(new_entry)


#TODO: Delete employee
#TODO: Update employee

