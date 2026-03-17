import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/Users/somitagarwal/Downloads/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
# x and y coordinate ke liye hume ye function likhne ki zarurat nhi hai kyuki humare
# paas already text file mein x and y values hai
# screen ko band krne ke liye mainloop() ke liye hota hai whi wala jo exitonclick() wala kaam

# screen.exitonclick()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name").capitalize()
# print(answer_state)

data = pd.read_csv("Day 25/50_states.csv")
# print(data)
count = 0

def correct_guess():
    count += 1
    answer_state = screen.textinput(title=f"{count}/50 states correct", prompt="What's another state's name").capitalize()

for i in range(0, 100):
    if answer_state in data["state"]:
        count += 1
        answer_state = screen.textinput(title=f"{count}/50 states correct", prompt="What's another state's name").capitalize()      
    else:
        answer_state = screen.textinput(title=f"{count}/50 states correct", prompt="What's another state's name").capitalize()



