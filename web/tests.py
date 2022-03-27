from django.test import TestCase

# Create your tests here.
from sqlite3 import connect
def get_data():
    conn = connect("db.sqlite3")

    return  conn.execute("SELECT * FROM web_employer").fetchall()

if __name__ == '__main__':
    conn =  connect("db.sqlite3")

    data = conn.execute("SELECT * FROM web_employer").fetchall()
    for i in data:
        print(i)