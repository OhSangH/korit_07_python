# Sierpinski Triangle - Turtle
# MODE: "chaos" (실시간 점찍기) | "recursive" (재귀 분할)

import turtle as tt
import random, math

# ===== 설정 =====
MODE = "chaos"           # "chaos" 또는 "recursive"
WIDTH, HEIGHT = 1100, 800
BG = "black"

# 공통 시각설정
SHOW_DRAWING = True      # 그리는 과정 보기
DRAW_DELAY = 0           # ms (값↑ = 느림)

# chaos 모드 설정
STEPS = 120000           # 점 개수
DOT_SIZE = 2             # 점 크기
UPDATE_EVERY = 300       # 화면 업데이트 주기(퍼포먼스용)

# recursive 모드 설정
DEPTH = 7                # 5~8 권장 (깊을수록 세밀)
FILL_BASE = (70, 200, 255)   # 저층 색
FILL_TOP  = (200, 120, 255)  # 고층 색

# ===== 유틸 =====
def setup_screen():
    screen = tt.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor(BG)
    tt.colormode(255)
    if SHOW_DRAWING:
        tt.tracer(1, DRAW_DELAY)
    else:
        tt.tracer(0, 0)
    return screen

def tri_vertices(side_frac=0.74):
    side = min(WIDTH, HEIGHT) * side_frac
    h = side * math.sqrt(3) / 2
    A = (0,  h/2 - 20)                 # 위 꼭짓점
    B = (-side/2, -h/2 - 20)           # 좌하
    C = ( side/2, -h/2 - 20)           # 우하
    return A, B, C

def lerp(a, b, t): return a + (b - a) * t
def lerp_color(c1, c2, t):
    return (int(lerp(c1[0], c2[0], t)),
            int(lerp(c1[1], c2[1], t)),
            int(lerp(c1[2], c2[2], t)))

def outline_triangle(t, A, B, C, color=(230,230,230)):
    t.pencolor(color); t.penup()
    t.goto(A); t.pendown(); t.goto(B); t.goto(C); t.goto(A); t.penup()

# ===== chaos game =====
def run_chaos():
    A, B, C = tri_vertices()
    verts = [A, B, C]

    # 시작점: 삼각형 내부 임의
    x, y = sum(v[0] for v in verts)/3, sum(v[1] for v in verts)/3

    pen = tt.Turtle(visible=False)
    pen.speed(0); pen.penup()
    pen.pencolor(200, 220, 255)

    # 외곽선
    out = tt.Turtle(visible=False); out.speed(0)
    outline_triangle(out, A, B, C)

    # 잔상 효과: 점 색을 천천히 보라->시안 그라데이션
    for i in range(STEPS):
        vx, vy = random.choice(verts)
        x = (x + vx) / 2.0
        y = (y + vy) / 2.0

        t = i / STEPS
        pen.pencolor(lerp_color((180,120,255), (120,230,255), t))
        pen.goto(x, y); pen.dot(DOT_SIZE)

        if not SHOW_DRAWING and (i % UPDATE_EVERY == 0):
            tt.update()

    if not SHOW_DRAWING:
        tt.update()

# ===== recursive =====
def fill_triangle(t, p1, p2, p3, color):
    t.fillcolor(color); t.pencolor(color)
    t.penup(); t.goto(p1); t.pendown()
    t.begin_fill()
    t.goto(p2); t.goto(p3); t.goto(p1)
    t.end_fill()
    t.penup()

def midpoint(a, b): return ((a[0]+b[0])/2.0, (a[1]+b[1])/2.0)

def sierpinski(t, p1, p2, p3, depth, max_depth, counter=[0]):
    if depth == 0:
        ratio = (max_depth - depth) / max_depth if max_depth else 1.0
        color = lerp_color(FILL_BASE, FILL_TOP, ratio)
        fill_triangle(t, p1, p2, p3, color)
        # 부분 업데이트(큰 깊이에서 애니메이션 유지)
        counter[0] += 1
        if SHOW_DRAWING and (counter[0] % 50 == 0):
            tt.update()
        return
    m12 = midpoint(p1, p2)
    m23 = midpoint(p2, p3)
    m31 = midpoint(p3, p1)
    sierpinski(t, p1, m12, m31, depth-1, max_depth, counter)
    sierpinski(t, m12, p2, m23, depth-1, max_depth, counter)
    sierpinski(t, m31, m23, p3, depth-1, max_depth, counter)

def run_recursive():
    A, B, C = tri_vertices()
    out = tt.Turtle(visible=False); out.speed(0)
    outline_triangle(out, A, B, C)

    t = tt.Turtle(visible=False)
    t.speed(0); t.penup()
    sierpinski(t, A, B, C, DEPTH, DEPTH)
    if not SHOW_DRAWING:
        tt.update()

# ===== 메인 =====
def main():
    setup_screen()
    if MODE == "chaos":
        run_chaos()
    else:
        run_recursive()
    tt.done()

if __name__ == "__main__":
    main()
