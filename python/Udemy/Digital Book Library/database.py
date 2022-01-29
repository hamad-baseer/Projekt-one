import sqlite3


def connection():
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books_data(ID INTEGER PRIMARY KEY, Title text, Author text, Year INTEGER, ISBN INTEGER)")
    connect.commit()
    connect.close()


def insert(title, author, year, isbn):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO books_data VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
    connect.commit()
    connect.close()


def view():
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM books_data")
    rows = cursor.fetchall()
    connect.close()
    return rows


def search(title="", author="", year="", isbn=""):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM books_data WHERE title=?, author=?, year=?, isbn=?", (title, author, year, isbn))
    rows = cursor.fetchall()
    connect.close()
    return rows


def delete(id):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("DELETE FROM books_data WHERE id=?", (id,))
    connect.commit()
    connect.close()


def update(id, title, author, year, isbn):
    connect = sqlite3.connect("books.db")
    cursor = connect.cursor()
    cursor.execute("UPDATE books_data SET title=?, author=?, year=?, isbn=? WHERE id=?", (id, title, author, year, isbn))
    connect.commit()
    connect.close()


connection()
#   insert('Visual Thinking', 'Willemien Brand', 2017, 9789063694531)
#   insert('Manhood', 'Cath Tate', 2014, 9781909396395)
#   insert('Wine Folly', 'Madeline Puckette', 2018, 9780525533894)
#   insert('MacOSX', 'Gaff', 2020, 47125324123)
