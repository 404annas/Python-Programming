from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.0)
    glEnd()
    glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Draw Point")
glutDisplayFunc(draw)
glutMainLoop()
