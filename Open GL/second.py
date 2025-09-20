from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, 0.0)
    glVertex2f(0.5, 0.0)
    glEnd()
    glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Draw Line")
glutDisplayFunc(draw)
glutMainLoop()
