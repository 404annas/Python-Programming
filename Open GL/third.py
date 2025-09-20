from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.7, 0.2)
    glVertex2f(0.0, 0.7)
    glVertex2f(-0.7, 0.2)
    glEnd()
    glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Draw Polygon")
glutDisplayFunc(draw)
glutMainLoop()
