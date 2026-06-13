from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message="Invalid Email Address")]) #validators = [DataRequired()] lagane se ye ise normal field se required field bana dega means jb tk ise nhi bharoge aage nhi badhoge
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)]) #PasswordField ka use krne se jo hum password likhenege wo encrypted form mein ******(dot dot) krke dikhega
    submit = SubmitField(label="Log In")

app = Flask(__name__)
app.secret_key = "1234"

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data)
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
