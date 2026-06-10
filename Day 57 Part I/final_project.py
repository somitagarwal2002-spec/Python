from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/blog/<num>')
def blog_function(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", posts=blog_data)

if __name__ == "__main__":
    app.run(debug=True)
