from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Float, String, Integer

app = Flask(__name__)

all_books = []

# Creating Database
class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'
    
with app.app_context():
    db.create_all()

# Creating a New Record
# with app.app_context():
#     new_book = Book(id=1, title='Harry Potter', author='J. K. Rowling', rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

@app.route('/')
def home():
    result = db.session.execute(db.select(Book))
    all_books = result.scalars().all()

    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=float(request.form["rating"])
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

