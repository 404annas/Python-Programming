from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(0.0, 0.6)
    glVertex2f(-0.6, -0.6)
    glVertex2f(0.6, -0.6)
    glEnd()
    glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Draw Triangle")
glutDisplayFunc(draw)
glutMainLoop()
