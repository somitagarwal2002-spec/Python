from flask import Flask

app = Flask(__name__)
# print(__name__) # ye batata hai kaun si current file run ho rhi hai

@app.route('/') # it is a decorator funciton
def hello_world():
    return "Hello World!"

@app.route('/bye')
def bye():
    return "Bye"

# @app.route('/<name>') #jo angular bracket mein likha hai use hum user se input lenge
# def hey(name):
#     return f"Hello {name}!"

# aise likhne se hota kya hai humara flask saare data ko body tag mein keval daal deta hai without any additional
# tag to hume apni website to aisi nhi chahiye jisme sb keval body tag ke andar hi likha ho to use correct krne 
# ke liye hum tag ko bhi chahe to usi mein add kr ke differentiate kr skte hai

@app.route('/<name>')
def hey(name):
    return f'<h1 style="text-align:center; color:red">Hey!</h1>'\
            '<p>This is a paragraph</p>' \
            '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExMThqcXd5ZHp4OHI3aGozNm0wcGRjemRqMDBmbjYwMWl1amo2eml5NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3z3Jqt42yS104gRc5c/giphy.gif" height=200>'


if __name__ == "__main__":
    app.run(debug=True) # debug on krne ke liye bss itna hi krna hota hai
