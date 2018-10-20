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
    print(rows)

    print('for x in rows')
    for x in rows:
        print(x)

    # Or directly: print(report)
    print('df.head')
    df = pd.DataFrame([[ij for ij in i] for i in rows])
    df.rename(columns={0: 'ID', 1: 'FirstName', 2: 'LastName', 3: 'Amount'}, inplace=True);
    df.head()

    names = df['FirstName']
    amounts = df['Amount']
    plt.bar(names, amounts)

    plt.title("Total expenses per employee")
    plt.show()


gen_report_ln()

# Export graphs to PDF.
# https://stackoverflow.com/questions/11328958/save-the-plots-into-a-pdf

connection.close()
