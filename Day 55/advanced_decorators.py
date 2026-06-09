from flask import Flask

app = Flask(__name__)
# print(__name__) # ye batata hai kaun si current file run ho rhi hai

def make_bold(function):
    def wrapper(*args, **kwargs):
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper(*args, **kwargs):
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function()}</u>"
    return wrapper

@app.route('/') # it is a decorator funciton
@make_bold
@make_emphasis
@make_underline
def hello_world():
    return "Hello World!"

@app.route('/bye')
def bye():
    return "Bye"

@app.route('/<int:name>') #jo angular bracket mein likha hai use hum user se input lenge
def hey(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)


