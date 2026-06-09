# Python Decorator Function
# Example

import time

def decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello")

@decorator_function
def bye():
    print("Bye Bye")

def hi():
    print("How are you")

say_hello()
bye()
hi()

# agr @ laga ke upar nhi likhna to hum baad mein bhi likh skte hai but @ wala zyada suitable aur easy to read hota hai

decorated_function = decorator_function(hi)
decorated_function()
