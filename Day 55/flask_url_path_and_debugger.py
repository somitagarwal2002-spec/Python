from flask import Flask

app = Flask(__name__)
# print(__name__) # ye batata hai kaun si current file run ho rhi hai

@app.route('/') # it is a decorator funciton
def hello_world():
    return "Hello World!"

@app.route('/bye')
def bye():
    return "Bye"

@app.route('/<int:name>') #jo angular bracket mein likha hai use hum user se input lenge
def hey(name):
    return f"Hello {name}!"
# by default <name> ki value wo string mein lega but agar hume specifically integer agar chahiye ho to hum 
# aise likh skte hai <int:name> to yha pr hum keval integer de skte hai aur agar humne string diya to ye
# error show krega 404 Not Found



# jaise hum koi bhi change krte hai apne program mein to hume uss change ko dekhne ke liye program ko band
# karke use dobara se run krna hota hai wo changes dekhne ke liye kyuki humara Debug: off hai yha pe to
# hume baar baar refresh aur baar baar run na krna pade uske liye hume Debug: on krna hoga

if __name__ == "__main__":
    app.run(debug=True) # debug on krne ke liye bss itna hi krna hota hai