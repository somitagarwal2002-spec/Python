
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    director: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(Integer)
    rating: Mapped[float] = mapped_column(Float)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return jsonify({"message":"Welcome to Movie REST API"})

@app.route("/movies", methods=["GET"])
def get_movies():
    movies = db.session.execute(db.select(Movie)).scalars().all()
    return jsonify([
        {
            "id":m.id,
            "title":m.title,
            "director":m.director,
            "year":m.year,
            "rating":m.rating
        } for m in movies
    ])

@app.route("/movie/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    return jsonify({
        "id":movie.id,
        "title":movie.title,
        "director":movie.director,
        "year":movie.year,
        "rating":movie.rating
    })

@app.route("/add", methods=["POST"])
def add_movie():
    data = request.json
    if not data:
        abort(400)
    exists = db.session.execute(
        db.select(Movie).where(Movie.title == data["title"])
    ).scalar()
    if exists:
        return jsonify({"error":"Movie already exists"}),409
    movie = Movie(
        title=data["title"],
        director=data["director"],
        year=data["year"],
        rating=data["rating"]
    )
    db.session.add(movie)
    db.session.commit()
    return jsonify({"message":"Movie Added"}),201

@app.route("/update/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    movie = db.get_or_404(Movie,movie_id)
    data = request.json
    movie.title=data["title"]
    movie.director=data["director"]
    movie.year=data["year"]
    movie.rating=data["rating"]
    db.session.commit()
    return jsonify({"message":"Movie Updated"})

@app.route("/patch/<int:movie_id>", methods=["PATCH"])
def patch_movie(movie_id):
    movie=db.get_or_404(Movie,movie_id)
    data=request.json
    if "title" in data:
        movie.title=data["title"]
    if "director" in data:
        movie.director=data["director"]
    if "year" in data:
        movie.year=data["year"]
    if "rating" in data:
        movie.rating=data["rating"]
    db.session.commit()
    return jsonify({"message":"Movie Patched"})

@app.route("/delete/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    movie=db.get_or_404(Movie,movie_id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"message":"Movie Deleted"})

@app.route("/search", methods=["GET"])
def search_movie():
    title=request.args.get("title")
    movie=db.session.execute(
        db.select(Movie).where(Movie.title==title)
    ).scalar()
    if not movie:
        return jsonify({"error":"Movie Not Found"}),404
    return jsonify({
        "id":movie.id,
        "title":movie.title,
        "director":movie.director,
        "year":movie.year,
        "rating":movie.rating
    })

@app.route("/top-rated", methods=["GET"])
def top_rated():
    movies=db.session.execute(
        db.select(Movie).where(Movie.rating>=8)
    ).scalars().all()
    return jsonify([
        {"title":m.title,"rating":m.rating}
        for m in movies
    ])

@app.route("/count")
def count_movies():
    total=len(db.session.execute(db.select(Movie)).scalars().all())
    return jsonify({"total_movies":total})

@app.route("/health")
def health():
    return jsonify({"status":"API Working"})

if __name__=="__main__":
    app.run(debug=True)
