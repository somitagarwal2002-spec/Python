from flask import Flask
from flask import render_template
import random
import datetime as dt

app = Flask(__name__)
current_year = dt.datetime.now().year

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
