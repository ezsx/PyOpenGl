import math
import glfw
import pygame as pg
from pygame.locals import *

from OpenGL.GLU import *
from OpenGL.GL import *

def lab2():
    edges = ((0, 1), (0, 5), (0, 3),
             (0, 1), (0, 7), (0, 3),

             (0, 2), (0, 5), (0, 4),
             (0, 2), (0, 8), (0, 4),

             (0, 3), (0, 8), (0, 2),
             (0, 3), (0, 6), (0, 2),

             (0, 4), (0, 6), (0, 1),
             (0, 4), (0, 7), (0, 1),
    )

    lines = (
        (0, 1), (1, 7), (1, 6), (0, 6),
        (0, 5), (0, 3), (3, 5), (0, 7),
        (0, 2), (0, 8), (2, 8), (2, 6),
        (0, 4), (4, 5), (4, 8), (7, 3),
    )

    def PyramidLines(height, width, edges, color):
        vertices = ((0.0, 2.5 + height, 0.0),
                    # outer
                    (1.0 + width, 1.0 + height, -1.0 - width),
                    (-1.0 - width, 1.0 + height, -1.0 - width),
                    (1.0 + width, 1.0 + height, 1.0 + width),
                    (-1.0 - width, 1.0 + height, 1.0 + width),
                    # inner
                    (0.0, 1.0 + height, 0.5),
                    (0.0, 1.0 + height, -0.5),
                    (0.5, 1.0 + height, 0.0),
                    (-0.5, 1.0 + height, 0.0))

        glBegin(GL_LINES)
        glColor4f(*color)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    def roof(height, width, edges, color):
        vertices = (
            (0.0, 2.5 + height, 0.0),
            # outer
            (1.0 + width, 1.0 + height, -1.0 - width),
            (-1.0 - width, 1.0 + height, -1.0 - width),
            (1.0 + width, 1.0 + height, 1.0 + width),
            (-1.0 - width, 1.0 + height, 1.0 + width),
            # inner
            (1.0, 1.0 + height, 1.0 + width),
            (1.0, 1.0 + height, -1.0 - width),
            (1.0, 1.0 + height, 1.0 + width),
            (-1, 1.0 + height, 1.0 + width)
        )

        glBegin(GL_TRIANGLES)
        glColor4f(*color)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    def Building(coords, color):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)

        sizeConstant = 1
        # base
        glVertex3fv((sizeConstant + coords[0],  coords[1], sizeConstant + coords[2]))
        glVertex3fv((-sizeConstant + coords[0], coords[1], sizeConstant + coords[2]))
        glVertex3fv((sizeConstant + coords[0], coords[1], -sizeConstant + coords[2]))

        glVertex3fv((-sizeConstant + coords[0], coords[1], -sizeConstant + coords[2]))
        glVertex3fv((-sizeConstant + coords[0], coords[1], sizeConstant + coords[2]))
        glVertex3fv((sizeConstant + coords[0], coords[1], -sizeConstant + coords[2]))

        glVertex3fv((sizeConstant + coords[0], sizeConstant + coords[1], sizeConstant + coords[2]))
        glVertex3fv((-sizeConstant + coords[0], sizeConstant + coords[1], sizeConstant + coords[2]))
        glVertex3fv((sizeConstant + coords[0], sizeConstant + coords[1], -sizeConstant + coords[2]))

        glVertex3fv((-sizeConstant + coords[0], sizeConstant + coords[1], -sizeConstant + coords[2]))
        glVertex3fv((-sizeConstant + coords[0], sizeConstant + coords[1], sizeConstant + coords[2]))
        glVertex3fv((sizeConstant + coords[0], sizeConstant + coords[1], -sizeConstant + coords[2]))

        edges = (
            (sizeConstant, sizeConstant),
            (-sizeConstant, sizeConstant),
            (-sizeConstant, -sizeConstant),
            (sizeConstant, -sizeConstant),
            (sizeConstant, sizeConstant),
        )
        for i in range(len(edges) - 1):
            glVertex3fv((edges[i][0] + coords[0], coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], coords[1], edges[i + 1][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], sizeConstant * 1.5 + coords[1], edges[i + 1][1] + coords[2]))

            glVertex3fv((edges[i][0] + coords[0], coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i][0] + coords[0], sizeConstant * 1.5 + coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], sizeConstant * 1.5 + coords[1], edges[i + 1][1] + coords[2]))

        glEnd()

    def window(coords, color):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)

        heightConstant = 0.3
        widthConstant = 0.2

        edges = (
            (heightConstant, widthConstant),
            (-heightConstant, widthConstant),
            (-heightConstant, -widthConstant),
            (heightConstant, -widthConstant),
            (heightConstant, widthConstant),
        )
        for i in range(len(edges) - 1):
            glVertex3fv((edges[i][0] + coords[0], coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], coords[1], edges[i + 1][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], heightConstant * 1.5 + coords[1], edges[i + 1][1] + coords[2]))

            glVertex3fv((edges[i][0] + coords[0], coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i][0] + coords[0], heightConstant * 1.5 + coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], heightConstant * 1.5 + coords[1], edges[i + 1][1] + coords[2]))

        glEnd()

    def door(coords, color):
        glBegin(GL_TRIANGLES)
        glColor4f(*color)

        heightConstant = 0.2
        widthConstant = 0.1
        zConstant = 0.5

        edges = (
            (heightConstant, widthConstant),
            (-heightConstant, widthConstant),
            (-heightConstant, -widthConstant),
            (heightConstant, -widthConstant),
            (heightConstant, widthConstant),
        )
        for i in range(len(edges) - 1):
            glVertex3fv((edges[i][0] + coords[0], coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], coords[1], edges[i + 1][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], zConstant * 1.5 + coords[1], edges[i + 1][1] + coords[2]))

            glVertex3fv((edges[i][0] + coords[0], coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i][0] + coords[0], zConstant * 1.5 + coords[1], edges[i][1] + coords[2]))
            glVertex3fv((edges[i + 1][0] + coords[0], zConstant * 1.5 + coords[1], edges[i + 1][1] + coords[2]))

        glEnd()

    def display():
        pg.init()
        display = (800, 600)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)

        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_LIGHT0)
        gluPerspective(50, (display[0] / display[1]), 0.1, 50.0)

        glTranslatef(0.0, -1.0, -10)
        glRotatef(30, 10, 0, 0)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            glRotatef(1, 0, 1, 0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            Building((0, 0, 0), (0.7, 0.7, 1.0, 1.0))

            window((0.35, 0.8, 0.81), (0., 0., 0.6, 1.0))

            window((-0.35, 0.8, -0.81), (0., 0., 0.6, 1.0))
            window((0.35, 0.8, -0.81), (0., 0., 0.6, 1.0))

            door((-0.2, 0., 0.92), (0.51, 0.25, 0., 1.0))

            Building((0, 1.5, 0), (0.7, 0.7, 1, 1.0))
            window((0.55, 1.5 + 0.5, 0.81), (0., 0., 0.6, 1.0))
            window((-0.55, 1.5 + 0.5, -0.81), (0., 0., 0.6, 1.0))
            window((0.55, 1.5 + 0.5, -0.81), (0., 0., 0.6, 1.0))

            window((-0.72, 1.5 + 0.5, .3), (0., 0., 0.6, 1.0))
            window((0.72, 1.5 + 0.5, -0.1), (0., 0., 0.6, 1.0))
            window((-0.72, 1.4, .3), (0., 0., 0.6, 1.0))


            roof(1.5 + 0.5, 0, edges, (1, 0.0, 0., 1.0))

            pg.display.flip()
            pg.time.wait(10)

    display()

lab2()