# 삼체문제(turtle 실시간 드로잉) - figure-eight & random
import turtle as tt
import math, random

# ====== 설정 ======
MODE = "figure_eight"      # "figure_eight" 또는 "random"
WIDTH, HEIGHT = 1100, 800
BG = "black"

# 애니메이션(그리는 과정 보기)
SHOW_DRAWING = True        # True면 매 스텝 그리는 모습 표시
DRAW_DELAY = 0             # ms (값이 클수록 느림)
UPD_EVERY = 2              # SHOW_DRAWING=False일 때 update 주기

# 물리 상수/스케일
G = 1.0                    # 중력상수(임의 단위)
M = [1.0, 1.0, 1.0]        # 세 질량(동일)
DT = 0.003                 # 시간 스텝(작을수록 안정/느림)
STEPS = 24000              # 적분 스텝 수
SOFTEN = 1e-4              # 연성(충돌/발산 방지용, figure-eight는 매우 작게)
SCALE = 260                # 화면 스케일(물리 좌표 -> 픽셀 변환 배율)

# ====== 유틸 ======
def vec_add(a, b):
    return [a[0]+b[0], a[1]+b[1]]

def vec_sub(a, b):
    return [a[0]-b[0], a[1]-b[1]]

def vec_mul(a, s):
    return [a[0]*s, a[1]*s]

def accel(positions):
    """각 질점의 가속도 계산 (뉴턴 만유인력)"""
    n = len(positions)
    a = [[0.0, 0.0] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            r = vec_sub(positions[j], positions[i])
            r2 = r[0]*r[0] + r[1]*r[1] + SOFTEN*SOFTEN
            inv_r3 = (r2 ** -1.5)
            s = G * M[j] * inv_r3
            a[i][0] += r[0]*s
            a[i][1] += r[1]*s
    return a

def verlet_step(pos, vel, dt):
    """속도 베르레(Verlet) 1스텝"""
    a0 = accel(pos)
    # r_{n+1}
    new_pos = [vec_add(pos[i], vec_add(vec_mul(vel[i], dt), vec_mul(a0[i], 0.5*dt*dt))) for i in range(3)]
    # a_{n+1}
    a1 = accel(new_pos)
    # v_{n+1}
    new_vel = [vec_add(vel[i], vec_mul(vec_add(a0[i], a1[i]), 0.5*dt)) for i in range(3)]
    return new_pos, new_vel

# ====== 초기조건 ======
def init_figure_eight():
    # 유명한 8자 궤도(Chenciner–Montgomery) 초기값 (G=1, m=1)
    # 참고: 두 입자는 서로 반대 위치, 세 번째는 원점. 두 입자 속도 동일, 세 번째는 -2배
    x = 0.97000436
    y = -0.24308753
    vx = 0.4662036850
    vy = 0.4323657300

    r1 = [-x, -y]
    r2 = [ x,  y]
    r3 = [ 0.0, 0.0]
    v1 = [ vx,  vy]
    v2 = [ vx,  vy]
    v3 = [-2*vx, -2*vy]
    return [r1, r2, r3], [v1, v2, v3]

def init_random():
    # 임의 초기조건 (약간 떨어뜨리고, 총 운동량은 0으로 보정)
    r = []
    for _ in range(3):
        r.append([random.uniform(-0.8, 0.8), random.uniform(-0.8, 0.8)])
    v = []
    for _ in range(3):
        v.append([random.uniform(-0.6, 0.6), random.uniform(-0.6, 0.6)])
    # 총 운동량 0 보정
    px = sum(M[i]*v[i][0] for i in range(3))
    py = sum(M[i]*v[i][1] for i in range(3))
    mtot = sum(M)
    for i in range(3):
        v[i][0] -= px/mtot
        v[i][1] -= py/mtot
    return r, v

# ====== 터틀 세팅 ======
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

def mk_body(color):
    t = tt.Turtle(visible=True)
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.pencolor(color)
    t.fillcolor(color)
    t.pensize(2)
    t.shape("circle")
    # 움직이는 점 표시용 작은 펜(별도)
    p = tt.Turtle(visible=True)
    p.hideturtle()
    p.penup()
    p.shape("circle")
    p.color(color)
    p.shapesize(0.5, 0.5)
    return t, p

def goto_draw(t, p, pos):
    x, y = pos[0]*SCALE, pos[1]*SCALE
    if not t.isdown():
        t.setpos(x, y); t.pendown()
    else:
        t.setpos(x, y)
    p.setpos(x, y)
    p.stamp()  # 점 표시

# ====== 메인 루프 ======
def main():
    setup_screen()
    # 초기 조건
    if MODE == "figure_eight":
        pos, vel = init_figure_eight()
        # figure-eight는 충돌이 잘 안 나서 연성 작게 유지
    else:
        pos, vel = init_random()

    colors = [(255,120,120), (140,230,200), (210,200,255)]
    trails = []
    points = []
    for c in colors:
        t, p = mk_body(c)
        trails.append(t)
        points.append(p)

    # 초기 위치 찍기
    for i in range(3):
        trails[i].penup()
        goto_draw(trails[i], points[i], pos[i])

    # 적분 & 드로잉
    for step in range(STEPS):
        pos, vel = verlet_step(pos, vel, DT)
        for i in range(3):
            goto_draw(trails[i], points[i], pos[i])

        if not SHOW_DRAWING:
            if step % UPD_EVERY == 0:
                tt.update()

    if not SHOW_DRAWING:
        tt.update()
    tt.done()

if __name__ == "__main__":
    main()
