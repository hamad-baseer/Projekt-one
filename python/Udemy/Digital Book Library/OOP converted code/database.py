import sqlite3


class Database:

    def __init__(self, database_file):
        self.connect = sqlite3.connect(database_file)
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books_data(ID INTEGER PRIMARY KEY, Title text, Author text, Year INTEGER, ISBN INTEGER)")
        self.connect.commit()

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO books_data VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
        self.connect.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM books_data")
        rows = self.cursor.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM books_data WHERE title=?, author=?, year=?, isbn=?", (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    def delete(self, id):
        self.cursor.execute("DELETE FROM books_data WHERE id=?", (id,))
        self.connect.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE books_data SET title=?, author=?, year=?, isbn=? WHERE id=?", (id, title, author, year, isbn))
        self.connect.commit()

    def __del__(self):
        self.connect.close()


#   insert('Visual Thinking', 'Willemien Brand', 2017, 9789063694531)
#   insert('Manhood', 'Cath Tate', 2014, 9781909396395)
#   insert('Wine Folly', 'Madeline Puckette', 2018, 9780525533894)
#   insert('MacOSX', 'Gaff', 2020, 47125324123)
