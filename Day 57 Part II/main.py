from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()

    blog_1_title = blog_data[0]["title"]
    blog_1_subtitle = blog_data[0]["subtitle"]

    blog_2_title = blog_data[1]["title"]
    blog_2_subtitle = blog_data[1]["subtitle"]

    blog_3_title = blog_data[2]["title"]
    blog_3_subtitle = blog_data[2]["subtitle"]

    return render_template("index.html", blog1=blog_1_title, blog1_sub=blog_1_subtitle,
                           blog2=blog_2_title, blog2_sub=blog_2_subtitle,
                           blog3=blog_3_title, blog3_sub=blog_3_subtitle)

@app.route('/blog/<int:num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()

    blog_1_title = blog_data[0]["title"]
    blog_1_body = blog_data[0]["body"]
    blog_1_subtitle = blog_data[0]["subtitle"]

    blog_2_title = blog_data[1]["title"]
    blog_2_body = blog_data[1]["body"]
    blog_2_subtitle = blog_data[1]["subtitle"]

    blog_3_title = blog_data[2]["title"]
    blog_3_body = blog_data[2]["body"]
    blog_3_subtitle = blog_data[2]["subtitle"]

    return render_template("post.html", number=num, blog1=blog_1_title, blog1_b=blog_1_body, blog1_sub=blog_1_subtitle,
                           blog2=blog_2_title, blog2_b=blog_2_body, blog2_sub=blog_2_subtitle,
                           blog3=blog_3_title, blog3_b=blog_3_body, blog3_sub=blog_3_subtitle)

if __name__ == "__main__":
    app.run(debug=True)
