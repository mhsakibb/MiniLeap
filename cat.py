from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# =========================
# Helpers
# =========================
def circle(x, y, r, seg=80):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(seg+1):
        ang = 2*math.pi*i/seg
        glVertex2f(x + r*math.cos(ang), y + r*math.sin(ang))
    glEnd()

def ellipse(x, y, rx, ry, seg=80):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(seg+1):
        ang = 2*math.pi*i/seg
        glVertex2f(x + rx*math.cos(ang), y + ry*math.sin(ang))
    glEnd()

# =========================
# CAT
# =========================
def draw_cat():

    # ===== BODY (rounded compact) =====
    glColor3f(0.95, 0.85, 0.75)
    ellipse(0.15, -0.05, 0.38, 0.22)

    # belly
    glColor3f(1.0, 0.92, 0.82)
    ellipse(0.1, -0.08, 0.22, 0.15)

    # ===== HEAD (connected naturally) =====
    glColor3f(0.95, 0.85, 0.75)
    circle(-0.35, 0.15, 0.22)

    # face
    glColor3f(1.0, 0.92, 0.82)
    ellipse(-0.38, 0.1, 0.16, 0.12)

    # ===== EARS =====
    glColor3f(1.0, 0.65, 0.2)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.5, 0.3)
    glVertex2f(-0.42, 0.55)
    glVertex2f(-0.3, 0.3)

    glVertex2f(-0.2, 0.3)
    glVertex2f(-0.32, 0.55)
    glVertex2f(-0.42, 0.3)
    glEnd()

    # inner ear
    glColor3f(1.0, 0.7, 0.8)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.47, 0.32)
    glVertex2f(-0.42, 0.48)
    glVertex2f(-0.34, 0.32)

    glVertex2f(-0.23, 0.32)
    glVertex2f(-0.32, 0.48)
    glVertex2f(-0.40, 0.32)
    glEnd()

    # ===== EYES (cute, close) =====
    glColor3f(1,1,1)
    circle(-0.43, 0.2, 0.055)
    circle(-0.30, 0.2, 0.055)

    glColor3f(0,0,0)
    circle(-0.43, 0.2, 0.028)
    circle(-0.30, 0.2, 0.028)

    # shine
    glColor3f(1,1,1)
    circle(-0.41, 0.23, 0.01)
    circle(-0.28, 0.23, 0.01)

    # ===== NOSE =====
    glColor3f(1.0, 0.55, 0.6)
    circle(-0.36, 0.12, 0.018)

    # ===== CAT SMILE (real shape) =====
    glColor3f(0,0,0)
    glLineWidth(2)
    glBegin(GL_LINE_STRIP)
    for i in range(20):
        t = i/19
        x = -0.42 + 0.12*t
        y = 0.1 - 0.03*math.sin(t*math.pi)
        glVertex2f(x, y)
    glEnd()

    # ===== CHEEKS =====
    glColor3f(1.0, 0.7, 0.7)
    circle(-0.5, 0.12, 0.025)
    circle(-0.25, 0.12, 0.025)

    # ===== WHISKERS (FIXED ANGLE) =====
    glColor3f(0.2,0.1,0.05)
    glBegin(GL_LINES)

    # left
    glVertex2f(-0.43, 0.15); glVertex2f(-0.6, 0.20)
    glVertex2f(-0.43, 0.15); glVertex2f(-0.6, 0.15)
    glVertex2f(-0.43, 0.15); glVertex2f(-0.6, 0.10)

    # right
    glVertex2f(-0.30, 0.15); glVertex2f(-0.15, 0.20)
    glVertex2f(-0.30, 0.15); glVertex2f(-0.15, 0.15)
    glVertex2f(-0.30, 0.15); glVertex2f(-0.15, 0.10)

    glEnd()

    # ===== LEGS (attached) =====
    xs = [0.0, 0.18, 0.32, 0.48]

    glColor3f(1.0, 0.65, 0.2)
    for x in xs:
        ellipse(x, -0.25, 0.06, 0.10)

    # paws
    glColor3f(1.0, 0.9, 0.8)
    for x in xs:
        circle(x, -0.33, 0.06)

    # ===== TAIL (smooth) =====
    for i in range(20):
        t = i/20
        x = 0.55 + 0.08*math.sin(math.pi*t)
        y = -0.05 + 0.5*t
        glColor3f(1.0, 0.65, 0.2)
        circle(x, y, 0.05)

    glColor3f(1.0, 0.9, 0.8)
    circle(0.55, 0.45, 0.06)

# =========================
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_cat()
    glutSwapBuffers()

def init():
    glClearColor(1,1,1,1)
    gluOrtho2D(-1,1,-1,1)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800,600)
    glutCreateWindow(b"Cute Cat FINAL FIX")

    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()