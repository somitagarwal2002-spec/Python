import sqlite3

db = sqlite3.connect("books_collection.db")
cursor = db.cursor()

# issko ek hi baar execute karaya jata hai jb hum apni table bana rhe ho ek baar jb ye execute ho jaye
# uske baaad ise comment out kr dete hai wrna "table books already exist" ka error aayega

# cursor.execute(
#     "CREATE TABLE books(" \
#     "id INTEGER PRIMARY KEY," \
#     "title varchar(250) NOT NULL UNIQUE," \
#     "author varchar(250) NOT NULL," \
#     "rating FLOAT NOT NULL)"
# )

cursor.execute(
    "INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', 9)," \
    "(2, 'Rich Dad Poor Dad', 'Robert Kiyosaki', 8)"
)

db.commit()
