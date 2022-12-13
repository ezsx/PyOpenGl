import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

def task3():


    def draw_sphere(x, y, z, radius, color):
        sphere = gluNewQuadric()
        glTranslatef(x, y, z)
        glColor3f(*color)
        gluSphere(sphere, radius, 20, 20)


    def display():
        pg.init()
        display = (1200, 900)
        scree = pg.display.set_mode(display, DOUBLEBUF | OPENGL)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])


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

            # multiply the current matrix by the get the new view matrix and store the final view matrix
            glMultMatrixf(viewMatrix)
            viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

            # apply view matrix
            glPopMatrix()
            glMultMatrixf(viewMatrix)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

            draw_sphere(0.0, 0.0, 0.0, 0.6, (0.35, 0.2, 0.12))    # head
            draw_sphere(0.0, 0.0, -0.7, 0.65, (0.35, 0.2, 0.12))    # body

            draw_sphere(-0.03, -0.6, 0.6, 0.1, (.0, 0., 0.))  # nose

            draw_sphere(0.6, 0.3, -0.5, 0.15, (0.2, 0.09, 0.047))   # left paw
            draw_sphere(0.0, 0.0, -0.1, 0.15, (0.2, 0.09, 0.047))
            draw_sphere(0.0, 0.0, -0.1, 0.15, (0.2, 0.09, 0.047))

            draw_sphere(-1.15, 0.0, -0.0, 0.15, (0.2, 0.09, 0.047))   # right paw
            draw_sphere(0.0, 0.0, 0.1, 0.15, (0.2, 0.09, 0.047))
            draw_sphere(0.0, 0.0, 0.1, 0.15, (0.2, 0.09, 0.047))

            draw_sphere(0.3, -0.0, -0.7, 0.15, (0.2, 0.09, 0.047))  # right leg
            draw_sphere(0.0, -0.1, -0.05, 0.15, (0.2, 0.09, 0.047))
            draw_sphere(0.0, -0.1, -0.05, 0.15, (0.2, 0.09, 0.047))

            draw_sphere(0.5, -0.0, -0.0, 0.15, (0.2, 0.09, 0.047))  # left leg
            draw_sphere(0.0, 0.1, 0.05, 0.15, (0.2, 0.09, 0.047))
            draw_sphere(0.0, 0.1, 0.05, 0.15, (0.2, 0.09, 0.047))

            draw_sphere(-0.05, -0.2, 1.37, 0.1, (1.0, 1.0, 1.0))    # right eye
            draw_sphere(-0.0, -0.1, 0.0, 0.03, (.0, .0, .0))

            draw_sphere(-0.4, 0.0, 0.0, 0.03, (.0, .0, .0))    # left eye
            draw_sphere(-0.0, 0.11, 0, 0.1, (1.0, 1.0, 1.0))

            draw_sphere(-0.2, 0.4, 0.35, 0.1, (0.2, 0.09, 0.047))  # right ear
            draw_sphere(0.02, 0.0, 0.1, 0.1, (0.2, 0.09, 0.047))
            draw_sphere(0.03, 0.0, 0.1, 0.1, (0.2, 0.09, 0.047))
            draw_sphere(0.05, 0.0, 0., 0.1, (0.2, 0.09, 0.047))
            draw_sphere(0.08, 0.0, -0.0, 0.1, (0.2, 0.09, 0.047))
            draw_sphere(0.05, 0.0, -0.05, 0.1, (0.2, 0.09, 0.047))
            draw_sphere(0.05, 0.0, -0.05, 0.1, (0.2, 0.09, 0.047))

            draw_sphere(0.3, 0.0, -0.00, 0.1, (0.2, 0.09, 0.047))   # left ear
            draw_sphere(0.05, 0.0, 0.05, 0.1, (0.2, 0.09, 0.047))
            draw_sphere(0.05, 0.0, 0.05, 0.1, (0.2, 0.09, 0.047))
            draw_sphere(0.08, 0.0, 0., 0.1, (0.2, 0.09, 0.047))
            draw_sphere(0.05, 0.0, 0., 0.1, (0.2, 0.09, 0.047))
            draw_sphere(0.03, 0.0, -0.1, 0.1, (0.2, 0.09, 0.047))
            draw_sphere(0.02, 0., -0.1, 0.1, (0.2, 0.09, 0.047))

            draw_sphere(-0.45, -0.4, -0.55, 0.2, (0.35, 0.2, 0.12))  # chew

            draw_sphere(-0.0, -0.15, -0.1, 0.03, (0., 0., 0.))    # mouth

            draw_sphere(-0.2, 0.26, 0.3, 0.2, (0.2, 0.09, 0.047))  # face fur
            draw_sphere(0.1, -0.01, 0.05, 0.2, (0.2, 0.09, 0.047))
            draw_sphere(0.05, -0.01, 0.00, 0.2, (0.2, 0.09, 0.047))
            draw_sphere(0.05, -0.01, 0.00, 0.2, (0.2, 0.09, 0.047))
            draw_sphere(0.05, 0.01, 0.0, 0.2, (0.2, 0.09, 0.047))
            draw_sphere(0.05, 0.01, 0.0, 0.2, (0.2, 0.09, 0.047))
            draw_sphere(0.05, -0.0, -0.05, 0.2, (0.2, 0.09, 0.047))
            draw_sphere(0.04, 0.003, -0.0, 0.2, (0.2, 0.09, 0.047))

            pg.display.flip()  # Update the screen
            pg.time.wait(10)

        pg.quit()

    display()


if __name__ == '__main__':
    task3()
