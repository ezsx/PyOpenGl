from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

import glfw
import pygame as pg
from pygame.locals import *

def lab4():
    pg.init()
    display = (1200, 900)
    scree = pg.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1]) # sphere color
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1]) # light color

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()
    displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pg.mouse.set_pos(displayCenter)

    pg.mouse.set_visible(False)
    up_down_angle = 0.0
    paused = False
    run = True

    ambient = (0, 0, 0, 1)
    lightpos = (2, 2, 2) # light source position
    coef = 0

    # Lighting
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_RETURN:
                    run = False
                if event.key == pg.K_PAUSE or event.key == pg.K_p:
                    paused = not paused
                    pg.mouse.set_pos(displayCenter)
            if not paused:
                if event.type == pg.MOUSEMOTION:
                    mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                pg.mouse.set_pos(displayCenter)

        if not paused:
            # get keys
            keypress = pg.key.get_pressed()
            # mouseMove = pygame.mouse.get_rel()

            # init model view matrix
            glLoadIdentity()

            # apply the look up and down
            up_down_angle += mouseMove[1] * 0.1
            glRotatef(up_down_angle, 1.0, 0.0, 0.0)

            # init the view matrix
            glPushMatrix()
            glLoadIdentity()
            ms = 0.06
            # apply the movment
            if keypress[pg.K_w]:
                glTranslatef(0, 0, ms)
            if keypress[pg.K_s]:
                glTranslatef(0, 0, -ms)
            if keypress[pg.K_d]:
                glTranslatef(-ms, 0, 0)
            if keypress[pg.K_a]:
                glTranslatef(ms, 0, 0)

            # apply the left and right rotation
            glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

        # light position for x y z, where x y z are the coordinates of the light source
        # glLightfv(GL_LIGHT0, GL_POSITION, lightpos)
        lightpos = (math.tan(coef), 2.0, math.tan(coef))
        # make the light from tan
        glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

        coef += 0.08

        glPushMatrix()

        # glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

        glutInit(sys.argv)

        glutSolidSphere(1, 20, 20)

        glPopMatrix()

        pg.display.flip()  # Update the screen
        pg.time.wait(10)

    pg.quit()

lab4()