import sqlite3
import pandas as pd

#connection = sqlite3.connect('database2.db')
conn = sqlite3.connect("database2.db")
crsr = conn.cursor()
#crsr = connection.cursor()


def sql_setup_dummy():

    sql_command = """CREATE TABLE emp (
    staff_number INTEGER PRIMARY KEY,
    fname VARCHAR(20),
    lname VARCHAR(30),
    gender CHAR(1),
    joining DATE);"""

    crsr.execute(sql_command)

    sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
    crsr.execute(sql_command)

    sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
    crsr.execute(sql_command)

    #connection.commit()
    #connection.close()

def print_db():
    crsr.execute("SELECT * FROM emp")
    ans = crsr.fetchall()
    for i in ans:
        print(i)

print_db()

df = pd.read_csv('employee_list.csv')

df.to_sql('new', conn)