from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Float, Integer, String

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


# Creating a New Record
with app.app_context():
    new_book = Book(id=1, title='Harry Potter', author='J. K. Rowling', rating=9.3)
    db.session.add(new_book)
    db.session.commit()

# Read all records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()

# Read a particular record by query
with app.app_context():
    result = db.session.execute(db.select(Book).where(Book.title == 'Harry Potter')).scalar()
    # jb hume ek hi record padhna hai to hum scalars nhi scalar likhte hai

# Updating a particular record by query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == 'Harry Potter')).scalar()
    book_to_update.title ='Harry Potter and the Philosophers Stone'
    db.session.commit()

# Updating a particular record by primary key
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)  
    book_to_update.title = 'Harry Potter and the Chamber of Secrets'
    db.session.commit()

# Delete a Particular record by primary key
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
     # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()

    