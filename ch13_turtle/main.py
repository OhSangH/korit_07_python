import turtle
from random import Random

t = turtle.Turtle()
screen = turtle.Screen()
WIDTH, HEIGHT = 1200, 800
random = Random()
colors = [
    'dark red',
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
    'light yellow'
]


def make_circle(x, y, num):
    t.pendown()
    t.circle(num)
    t.penup()
    # t.goto(x, y)


def make_diagram(num):
    for n in range(num):
        draw_dotted_line(70)
        t.left(360 / num)

def draw_dotted_line(num):
    have_shape = False
    cnt = 0
    flag_cnt = num//10
    for _ in range(num):
        if have_shape:
            t.penup()
            t.forward(1)
        else:
            t.pendown()
            t.forward(1)
        cnt += 1
        if cnt == flag_cnt:
            have_shape = not have_shape
            cnt = 0

screen.setup(WIDTH, HEIGHT)
t.hideturtle()
screen.bgcolor('black')
t.color('pink')
t.speed(0)

# for i in range(500):
#     t.circle(i)
#     t.left(5)
# print(t.heading())

# t.penup()
# t.goto(-5, -(HEIGHT / 2))
# t.pendown()

# for i in range(3, 50):
#     make_diagram(i)
#     t.color(random.choice(colors))
def draw_spirograph(num):
    for i in range(num):
        t.circle(100)
        t.setheading(t.heading()+ 360/num)
        t.color(random.choice(colors))

# draw_spirograph(0.5)
for i in range(200):
    t.forward(i)
    t.setheading(t.heading() + i)
    # t.color(random.choice(colors))

screen.exitonclick()
