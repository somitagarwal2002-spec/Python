from flask import Flask

app = Flask(__name__)
print(__name__) # ye batata hai kaun si current file run ho rhi hai

@app.route('/')

def hello_world():
    return "Hello World!"
if __name__ == "__main__":
    app.run()
    # app.run() likhne se jo hume environment variable bana ke likhna pad rha tha terminal pr usse hum
    # bach gye wrna hume ye likhna hota -> export FLASK_APP="Day 54 Flask/hello_flask.py" aur
    # uske baad -> flask run
    # in the terminal
