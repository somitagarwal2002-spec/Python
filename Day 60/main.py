from flask import Flask, render_template, request
import requests

app = Flask(__name__)

n_point_url = "https://api.npoint.io/5868ee9f7f74bbb450ce"
posts = requests.get(n_point_url).json()
# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/login', methods=['POST'])
# def received_data():
#     name = request.form["username"]
#     password = request.form["password"]
#     return f"<h1>Name: {name} Password: {password}</h1>"

@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/post.html/<int:index>')
def post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__=="__main__":
    app.run(debug=True)
