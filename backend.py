import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn. cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, year, author, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn. cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, year, author, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn. cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title= "", author= "", year= "", isbn= ""):
    conn = sqlite3.connect("books.db")
    cur = conn. cursor()
    cur.execute("SELECT * from book where title = ? or author = ? or year = ? or isbn = ?", 
    (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn. cursor()
    cur.execute("DELETE from book where id=?", (id,)) 
    conn.commit()
    conn.close()

def update(id,title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn. cursor()
    cur.execute("UPDATE book SET TITLE=?, AUTHOR=?, YEAR=?, ISBN=? where id=?", (title, author, year, isbn, id)) 
    conn.commit()
    conn.close()    

connect()
# insert("The sea", "JOhn Tablet", 1918, 913139393933)
# insert("Harry Potter", "Sure", 1918, 913139393933)
print(view())
print(search(author="Sure"))
print("*****************")
delete(4)
print(view())
update(11, "HP", "Sheldon", 2000, 1234)
print(view())