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

data = pd.read_csv("Day 25/50_states.csv")
all_states = data.state.to_list()
guessed_state =[]
missing_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Guessed", 
                                    prompt="What's another state's name").title()
    print(answer_state)

    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        # print(missing_state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("Day 25/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item()) # OR t.write(answer_state)


count = 0
screen.exitonclick()
# def correct_guess():
#     count += 1
#     answer_state = screen.textinput(title=f"{count}/50 states correct", prompt="What's another state's name").capitalize()

# for i in range(0, 100):
#     if answer_state in data["state"]:
#         count += 1
#         answer_state = screen.textinput(title=f"{count}/50 states correct", prompt="What's another state's name").capitalize()      
#     else:
#         answer_state = screen.textinput(title=f"{count}/50 states correct", prompt="What's another state's name").capitalize()



