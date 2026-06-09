from flask import Flask
from flask import render_template

AGIFY_API = "https://api.agify.io"
GENDERIZE_API = "https://api.genderize.io"

app = Flask(__name__)

@app.route('/')
def home():
    return "Nothing"

@app.route('/guess/<name>')
def work(name):
    return render_template("gender_age.html", username=name)

if __name__ == "__main__":
    app.run(debug=True)
