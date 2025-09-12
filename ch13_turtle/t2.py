# turtle 프랙탈/프랙쳐 스타일 (실시간 드로잉)
import turtle as tt
import random

# ===== 설정 =====
MODE = "tree"          # "tree" 또는 "snowflake"
BG_COLOR = "black"
WIDTH, HEIGHT = 1200, 800

SHOW_DRAWING = True    # 그리는 과정 보기
DRAW_DELAY = 0         # ms 단위 지연 (값이 클수록 느림)
SPEED = 10              # 1(매우 느림) ~ 10(빠름), 0은 순간

def setup_screen():
    screen = tt.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor(BG_COLOR)
    tt.colormode(255)
    if SHOW_DRAWING:
        tt.tracer(1, DRAW_DELAY)   # 실시간 애니메이션
    else:
        tt.tracer(False)           # 한 번에 렌더
    return screen

def lerp(a, b, t): return a + (b - a) * t
def lerp_color(c1, c2, t):
    return (int(lerp(c1[0], c2[0], t)),
            int(lerp(c1[1], c2[1], t)),
            int(lerp(c1[2], c2[2], t)))

# ===== 1) 균열 느낌 트리 =====
def draw_fracture_tree(t, length, depth, max_depth):
    if depth == 0 or length < 2:
        return
    c1 = (0, 255, 210); c2 = (174, 0, 255)
    ratio = (max_depth - depth) / max_depth
    color = lerp_color(c1, c2, ratio)
    t.pencolor(color)
    t.pensize(max(1, int(3 * (depth / max_depth) + 1)))

    t.forward(length)

    branches = random.randint(2, 3)
    base = random.uniform(18, 32)
    angles = []
    for i in range(branches):
        sign = -1 if i % 2 == 0 else 1
        angles.append(sign * (base + random.uniform(-6, 10)))

    for ang in angles:
        t.left(ang)
        next_len = length * random.uniform(0.66, 0.78)
        draw_fracture_tree(t, next_len, depth - 1, max_depth)
        t.right(ang)

    t.backward(length)

def run_tree():
    t = tt.Turtle(visible=False)
    t.speed(SPEED)
    t.penup()
    t.setpos(0, -HEIGHT // 2 + 50)
    t.setheading(90)
    t.pendown()

    max_depth = 10
    trunk = HEIGHT * 0.23
    draw_fracture_tree(t, trunk, max_depth, max_depth)
    if not SHOW_DRAWING: tt.update()

# ===== 2) 코흐 스노우플레이크 =====
def koch_segment(t, order, length):
    if order == 0:
        t.forward(length)
        return
    length /= 3.0
    koch_segment(t, order-1, length)
    t.left(60)
    koch_segment(t, order-1, length)
    t.right(120)
    koch_segment(t, order-1, length)
    t.left(60)
    koch_segment(t, order-1, length)

def run_snowflake(order=4):  # order 5 이상이면 매우 오래 걸릴 수 있음
    t = tt.Turtle(visible=False)
    t.speed(SPEED)
    t.pensize(2)
    colors = [(200,200,255), (160,220,255), (220,200,255)]

    side = min(WIDTH, HEIGHT) * 0.42
    t.penup()
    t.setpos(-side/2, side/3)
    t.setheading(0)
    t.pendown()

    for i in range(3):
        t.pencolor(colors[i % len(colors)])
        koch_segment(t, order, side)
        t.right(120)
    if not SHOW_DRAWING: tt.update()

def main():
    setup_screen()
    if MODE.lower() == "tree":
        run_tree()
    else:
        run_snowflake(order=4)
    tt.done()

if __name__ == "__main__":
    main()
