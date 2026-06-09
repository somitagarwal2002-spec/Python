# First Class Objects

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(cal_function, a, b):
    return cal_function(a, b)
# Python functions are first class objexts means python functions can be used as am argument

result = calculate(add, 2, 3)
print(result)

result_next = calculate(subtract, 2, 3)
print(result_next)

# Nested Function - Functions written inside a function is known as nested function

def outer_function():
    print("I am outer function")

    def nested_function():
        print("I am nested function written inside a function")
    
    nested_function()


# nested_function() hum nested function ko aise hi call nhi kr skte isiliye hum ise outer function ke andar hi call karenge

outer_function()

# Functions can be returned from other functions

def outer_function():
    print("I am outer function")

    def nested_function():
        print("I am nested function written inside a function")
    
    return nested_function # bss yha paranthesis nhi lagana hota ()

result = outer_function()
result()
print(result)
# print wale ka output ye hai 
# I am outer function
# <function outer_function.<locals>.nested_function at 0x102ae1800>
