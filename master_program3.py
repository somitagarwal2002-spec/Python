from datetime import date
from functools import wraps

from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, ForeignKey
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, URL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

ckeditor = CKEditor(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    posts = relationship("BlogPost", back_populates="author")

class BlogPost(db.Model):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    subtitle: Mapped[str] = mapped_column(String(250))
    body: Mapped[str] = mapped_column(Text)
    img_url: Mapped[str] = mapped_column(String(500))
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class CreatePostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Body", validators=[DataRequired()])
    submit = SubmitField("Publish")

def admin_only(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return abort(403)
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return wrapper

@app.route("/")
def home():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", posts=posts, current_user=current_user)

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing = db.session.execute(
            db.select(User).where(User.email == form.email.data)
        ).scalar()
        if existing:
            flash("Email already registered.")
            return redirect(url_for("login"))
        password = generate_password_hash(
            form.password.data,
            method="pbkdf2:sha256",
            salt_length=8
        )
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            password=password
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash("Registration Successful")
        return redirect(url_for("home"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(
            db.select(User).where(User.email == form.email.data)
        ).scalar()
        if not user:
            flash("Email not found")
            return redirect(url_for("login"))
        if not check_password_hash(user.password, form.password.data):
            flash("Wrong Password")
            return redirect(url_for("login"))
        login_user(user)
        flash("Login Successful")
        return redirect(url_for("home"))
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged Out")
    return redirect(url_for("home"))

@app.route("/new-post", methods=["GET","POST"])
@login_required
@admin_only
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash("Post Created")
        return redirect(url_for("home"))
    return render_template("make-post.html", form=form)

@app.route("/edit/<int:post_id>", methods=["GET","POST"])
@login_required
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body
    )
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.img_url = form.img_url.data
        post.body = form.body.data
        db.session.commit()
        flash("Post Updated")
        return redirect(url_for("home"))
    return render_template("make-post.html", form=form, is_edit=True)

@app.route("/delete/<int:post_id>")
@login_required
@admin_only
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post Deleted")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
