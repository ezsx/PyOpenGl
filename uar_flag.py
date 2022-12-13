import pygame as pygame
import random as random
import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# initialize pygame


def rect(fromX, toX, fromY, toY, sc):
    glBegin(GL_QUADS)
    glVertex2f(fromX * sc, fromY * sc)
    glVertex2f(toX * sc, fromY * sc)
    glVertex2f(toX * sc, toY * sc)
    glVertex2f(fromX * sc, toY * sc)
    glEnd()


def main():
    pygame.init()
    pygame.display.set_caption('ФЛАГ ЮАР')
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(-0.75, 0.0, -3)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        scale = 1

        glColor4f(0.0, 1.0, 0.0, 0.0)
        rect(-1, 1, 0, -2, scale)

        # draw red rectangle
        glColor4f(1.0, 0.0, 0.0, 0.0)
        rect(-1, 1, 1, 0, scale)

        # draw blue rectangle on the bottom of the red one
        glColor4f(0.0, 0.0, 1.0, 0.0)
        rect(-1, 1, 0.5, 0, scale)

        # past white rectangle
        glColor4f(1.0, 1.0, 1.0, 0.0)
        glBegin(GL_TRIANGLES)
        glVertex2f(-1.2 * scale, -0.6 * scale)
        glVertex2f(-1.2 * scale, 1.6 * scale)
        glVertex2f(0.1 * scale, 0.5 * scale)
        glEnd()

        # past big green trianfle on the left of
        glColor4f(0.0, 1.0, 0.0, 0.0)
        glBegin(GL_TRIANGLES)
        glVertex2f(-1 * scale, -0.3 * scale)
        glVertex2f(-1 * scale, 1.3 * scale)
        glVertex2f(-0.1 * scale, 0.5 * scale)
        glEnd()

        # past green rectangle on the right of the red one
        glColor4f(0.0, 1.0, 0.0, 0.0)
        rect(0, 0.1, 0.1, 0.1, scale)
        # where coordinates are in range [-1, 1] in both axes
        # x axis is horizontal, y axis is vertical
        # (0, 0) is the center of the screen
        # (1, 1) is the top right corner of the screen

        glColor4f(1.0, 0.5, 0.0, 0.0)
        glBegin(GL_TRIANGLES)
        glVertex2f(-0.9 * scale, 0 * scale)
        glVertex2f(-1.0 * scale, 1.1 * scale)
        glVertex2f(-0.4 * scale, 0.5 * scale)
        glEnd()

        glColor4f(0.0, 0.0, 0.0, 0.0)
        glBegin(GL_TRIANGLES)

        glVertex2f(-1 * scale, 0 * scale)
        glVertex2f(-1.0 * scale, 1.0 * scale)
        glVertex2f(-0.5 * scale, 0.5 * scale)
        # paste black triangle on the left rectangle
        glEnd()

        # past green rectangle in the middle at all
        glColor4f(0.0, 1.0, 0.0, 0.0)
        rect(-0.4, 1, 0.35, 0.65, scale)

        # white rectangle
        glColor4f(1.0, 1.0, 1.0, 0.0)
        rect(-0.25, 1, 0.65, 0.75, scale)
        glColor4f(1.0, 1.0, 1.0, 0.0)
        rect(-0.25, 1, 0.25, 0.35, scale)
        # set black rectangles
        glColor4f(0.0, 0.0, 0.0, 0.0)
        rect(-1, 1, 1, 2, scale)

        glColor4f(0.0, 0.0, 0.0, 0.0)
        rect(-1, 1, 0, -2, scale)

        pygame.display.flip()
        pygame.time.wait(1)


if __name__ == '__main__':
    main()
