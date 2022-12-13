import random
import time
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


width = 500
height = 500
random_number = 0
turned = 0
angle = 0

switch = False

vertices = [(-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)]
faces = [(4, 0, 3, 7), (1, 0, 4, 5), (0, 1, 2, 3), (1, 5, 6, 2), (3, 2, 6, 7), (5, 4, 7, 6)]
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1), (0, 0, 0)]
textureCoords = [(1, 1), (1, 0), (0, 0), (0, 1)]
normals = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(0, 1, 0)
    glEnd()

def draw_horizontal(mult):
    glPushMatrix()
    glRotatef(mult*90, 1, 0, 0)
    draw_triangle()
    glPopMatrix()

def draw_rectangle(mult):
    glBegin(GL_QUADS)
    glVertex3f(-0, -0, 0)
    glVertex3f(mult, -0, 0)
    glVertex3f(mult * 0.5, mult * 2, 0)
    glVertex3f(-mult * 0.5, mult * 3, 0)
    glEnd()

def draw_horizontal_rect(mult):
    glPushMatrix()
    glRotatef(mult*90, 1, 0, 0)
    draw_rectangle(1)
    glPopMatrix()

def draw_cube():
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            # glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_plane():
    glTranslatef(0, -0.07, 0)
    # 1 sphere
    for _ in range(5):
        glutSolidSphere(0.35, 20, 20)
        glTranslatef(-0.01, 0, 0)
    glTranslatef(-0.3, 0.07, 0)
    size = 0.5
    mult = 0.99
    # body of plane
    for _ in range(60):
        glutSolidSphere(size, 20, 20)
        glTranslatef(-0.05, 0, 0)
        size *= mult
    size = 0.15
    mult = 0.97
    # padding coordinates
    for _ in range(30):
        glTranslatef(-0.01, 0.03, 0)
        # glutSolidSphere(size, 50, 20) solid tail, bad looking
        size *= mult

    # padding
    glTranslatef(0.2, -0.8, 0)
    draw_triangle() # tail vertical
    glTranslatef(0.2, -0.2, 0)
    draw_horizontal(1) # tail horizontal right
    draw_horizontal(-1) # tail horizontal left
    glTranslatef(1.6, 0, 0) # padding
    draw_horizontal_rect(1) # wing horizontal right
    draw_horizontal_rect(-1) # wing horizontal left


def draw_shapes():
    global turned, switch, random_number, angle
    glDisable(GL_TEXTURE_2D)
    glPushMatrix()

    if turned >= 90:
        random_number = random.randint(0, 2)
        turned = angle = 0

    glRotatef(angle, 0.5, 0, 0)
    # turned += 1
    angle += 2
    # draw_3d_rectangle()
    # draw_cube()
    draw_plane()
    # glutSolidSphere(0.5, 20, 20)
    # glutSolidTorus(0.4, 0.8, 25, 25)
    glLightModeliv(GL_LIGHT_MODEL_TWO_SIDE, 1)

    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    glPushMatrix()

    glTranslatef(-3, 0, 0)
    glPopMatrix()





def showScreen():
    global width, height

    glClearColor(0, 0, 0, 1)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 1, 1, 1))
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.0, 1.0, 0.0, 1.0))
    glEnable(GL_COLOR_MATERIAL)

    greencolor = (0.2, 0.8, 0.0, 0.8)

    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 4, 0, 1))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (0.0, 1.0, 0.0, 1.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 0))
    glEnable(GL_BLEND)

    # glLightfv(GL_LIGHT0, GL_COLOR, greencolor)

    glEnable(GL_DEPTH_TEST)
    # draw_cube()
    draw_shapes()
    glutSwapBuffers()


def reshapeWindow(x, y):
    global width, height
    width = x
    height = y
    print(x, y)
    glutReshapeWindow(width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.0001, 1000)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -7)


def keyboard(key, x_pos, y_pos):
    print(key, x_pos, y_pos)


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 500)
wind = glutCreateWindow("OpenGL")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutReshapeFunc(reshapeWindow)
glutKeyboardFunc(keyboard)
gluPerspective(45, (width / height), 0.0001, 100)


while True:
    glutMainLoopEvent()
    glutPostRedisplay()
    time.sleep(0.01)