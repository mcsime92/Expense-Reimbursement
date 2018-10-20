import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

connection = sqlite3.connect('employee_list.db')
cursor = connection.cursor()


def gen_report_ln():
    sql_command = """SELECT emp.id, emp.first_name, emp.last_name, expenses.amount
                    FROM emp
                    LEFT JOIN expenses
                    ON emp.last_name = expenses.last_name AND emp.first_name = expenses.first_name """

    cursor.execute(sql_command)

    rows = cursor.fetchall()

    df = pd.DataFrame([[ij for ij in i] for i in rows])
    df.rename(columns={0: 'ID', 1: 'FirstName', 2: 'LastName', 3: 'Amount'}, inplace=True)

    names = df['FirstName']
    amounts = df['Amount']

    f = plt.figure()
    plt.bar(names, amounts)
    plt.title("Total expenses per employee")

    plt.show()

    print_to_pdf = input("Would you like to print it to PDF ? Type: Yes or No: ")
    print_to_pdf_lowercase = print_to_pdf.lower()
    if print_to_pdf_lowercase == "yes":

        f.savefig("Expense_report.pdf", bbox_inches='tight')
    else:
        pass


gen_report_ln()

connection.close()
