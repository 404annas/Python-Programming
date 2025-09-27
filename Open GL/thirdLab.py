from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

angle = 0.0
scale = 1.0
tx, ty = 0.0, 0.0

def draw():
    global angle, scale, tx, ty
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Apply transformations
    glTranslatef(tx, ty, 0.0)  # Translation
    glRotatef(angle, 0.0, 0.0, 1.0)  # Rotation around z-axis
    glScalef(scale, scale, 1.0)  # Scaling

    # Draw a triangle
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0, 1, 0)
    glVertex2f(0.5, -0.5)
    glColor3f(0, 0, 1)
    glVertex2f(0.0, 0.5)
    glEnd()

    glutSwapBuffers()

def keyboard(key, x, y):
    global angle, scale, tx, ty
    key = key.decode("utf-8")
    if key == 'q':
        sys.exit()
    elif key == 't':  # translate
        tx += 0.1
        ty += 0.1
    elif key == 'r':  # rotate
        angle += 15
    elif key == 's':  # scale
        scale += 0.1
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Lab-3: 2D Transformations")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(draw)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
