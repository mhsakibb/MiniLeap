from OpenGL.GL import *
from OpenGL.GLUT import (
    glutInit, glutInitDisplayMode, glutInitWindowSize,
    glutCreateWindow, glutDisplayFunc, glutKeyboardFunc,
    glutTimerFunc, glutMainLoop, glutBitmapCharacter,
    glutPostRedisplay, GLUT_SINGLE, GLUT_RGB,
    GLUT_BITMAP_HELVETICA_18
)
import random
import math


# =========================
# Game State
# =========================
cat_x = -0.7
cat_y = -0.7
velocity_y = 0.0
gravity = -0.006
jump_power = 0.09
ground_y = -0.7
jumping = False
jump_count = 0   # for double jump

score = 0
game_over = False

obstacles = [
    [1.0, -0.75, 0.08, 0.15],
    [1.8, -0.75, 0.08, 0.15]
]

coins = [
    [1.2, -0.3, 0.04],
    [2.0, 0.0, 0.04]
]


# =========================
# Draw Helpers
# =========================
def draw_rect(x, y, w, h):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + w, y)
    glVertex2f(x + w, y + h)
    glVertex2f(x, y + h)
    glEnd()


def draw_circle(cx, cy, r):
    glBegin(GL_POLYGON)
    for i in range(50):
        angle = 2 * math.pi * i / 50
        glVertex2f(
            cx + r * math.cos(angle),
            cy + r * math.sin(angle)
        )
    glEnd()


def draw_text(x, y, text):
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))


# =========================
# Cat Character 😺
# =========================
def draw_cat(x, y):
    # body
    glColor3f(1.0, 0.6, 0.2)
    draw_rect(x, y, 0.12, 0.10)

    # head
    draw_circle(x + 0.06, y + 0.14, 0.05)

    # ears
    glBegin(GL_TRIANGLES)
    glVertex2f(x + 0.03, y + 0.18)
    glVertex2f(x + 0.045, y + 0.24)
    glVertex2f(x + 0.06, y + 0.18)

    glVertex2f(x + 0.06, y + 0.18)
    glVertex2f(x + 0.075, y + 0.24)
    glVertex2f(x + 0.09, y + 0.18)
    glEnd()

    # eyes
    glColor3f(0, 0, 0)
    draw_circle(x + 0.045, y + 0.15, 0.007)
    draw_circle(x + 0.075, y + 0.15, 0.007)

    # tail
    glColor3f(1.0, 0.6, 0.2)
    draw_rect(x - 0.03, y + 0.03, 0.03, 0.01)


# =========================
# Collision
# =========================
def collide_rect(px, py, ox, oy, ow, oh):
    return (
        px + 0.12 > ox and
        px < ox + ow and
        py + 0.15 > oy and
        py < oy + oh
    )


def collide_coin(px, py, cx, cy, r):
    dx = (px + 0.06) - cx
    dy = (py + 0.08) - cy
    return dx * dx + dy * dy < (r + 0.06) ** 2


# =========================
# Display
# =========================
def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # background
    glClearColor(0.5, 0.8, 1.0, 1.0)

    # ground
    glColor3f(0.2, 0.8, 0.2)
    draw_rect(-1, -0.8, 2, 0.1)

    # cat
    draw_cat(cat_x, cat_y)

    # obstacles
    glColor3f(0.8, 0.2, 0.2)
    for obs in obstacles:
        draw_rect(obs[0], obs[1], obs[2], obs[3])

    # coins
    glColor3f(1.0, 0.9, 0.0)
    for coin in coins:
        draw_circle(coin[0], coin[1], coin[2])

    # score
    glColor3f(0, 0, 0)
    draw_text(-0.95, 0.9, f"Score: {score}")

    if game_over:
        draw_text(-0.15, 0.0, "GAME OVER | Press R")

    glFlush()


# =========================
# Update Loop
# =========================
def update(value):
    global cat_y, velocity_y, jumping, jump_count
    global score, game_over

    if not game_over:
        # jump physics
        if jumping:
            velocity_y += gravity
            cat_y += velocity_y

            if cat_y <= ground_y:
                cat_y = ground_y
                velocity_y = 0
                jumping = False
                jump_count = 0   # reset double jump

        # move obstacles
        for obs in obstacles:
            obs[0] -= 0.012

            if obs[0] < -1.2:
                obs[0] = random.uniform(1.0, 2.2)

            if collide_rect(cat_x, cat_y, *obs):
                game_over = True

        # move coins
        for coin in coins:
            coin[0] -= 0.012

            if coin[0] < -1.2:
                coin[0] = random.uniform(1.0, 2.2)
                coin[1] = random.uniform(-0.2, 0.4)

            if collide_coin(cat_x, cat_y, *coin):
                score += 1
                coin[0] = random.uniform(1.0, 2.2)
                coin[1] = random.uniform(-0.2, 0.4)

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)


# =========================
# Controls
# =========================
def keyboard(key, x, y):
    global jumping, velocity_y, jump_count
    global game_over

    key = key.decode().lower()

    # double jump
    if key == ' ' and jump_count < 2 and not game_over:
        jumping = True
        velocity_y = jump_power
        jump_count += 1

    if key == 'r' and game_over:
        restart()


def restart():
    global game_over, score, cat_y
    global jumping, velocity_y, jump_count

    game_over = False
    score = 0
    cat_y = ground_y
    jumping = False
    velocity_y = 0
    jump_count = 0

    obstacles[0][0] = 1.0
    obstacles[1][0] = 1.8
    coins[0][0] = 1.2
    coins[1][0] = 2.0


# =========================
# Start
# =========================
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(1000, 500)
glutCreateWindow(b"Cat Coin Runner")

glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutTimerFunc(16, update, 0)

glutMainLoop()