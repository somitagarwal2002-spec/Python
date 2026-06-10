from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Nothing"

@app.route('/guess/<name>')
def work(name):
    age_url = f"https://api.agify.io/?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    ages = age_data["age"]

    gender_url = f"https://api.genderize.io/?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    genders = gender_data["gender"]
    
    return render_template("gender_age.html", username=name, username_gender=genders["gender"], username_age=ages["age"])

if __name__ == "__main__":
    app.run(debug=True)
