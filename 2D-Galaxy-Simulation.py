'''
    2D Güneş Sistemi Simülasyonu
'''
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys

rangleSun = 0.0  # Güneşin kendi Etrafında Dönme Açısı için global değişken
rangleEarth = 0  # DÜnyanın kendi Etrafında Dönme Açısı için global değişken
rangleMoon = 0  # Ayın kendi Etrafında Dönme Açısı için global değişken
tetaEarth = 0.0  # Dünyanın Güneş Etrafında Dönme Açısı için global değişken
tetaMoon = 0.0  # Ayın dünya Etrafında Dönme Açısı için global değişken


def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)


def DrawGLScene():
    global rangleSun
    global tetaEarth
    global rangleEarth
    global rangleMoon
    global tetaMoon

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Güneşin orijinde oluşturulması ve kendi etrafında dönmesi
    glPushMatrix()
    glColor(1, 1, 0)  # Güneş için sarı rengi
    glRotatef(rangleSun, 0, 0, 1)
    glutSolidSphere(1, 20, 20)
    glPopMatrix()

    # Dünyanın oluşturulması ve hem kendi hem de güneş etrafında dönmesi
    glPushMatrix()
    glColor(0, 0.8, 1)  # Dünya için açık mavi rengi
    glTranslatef((3 * math.cos(tetaEarth)), (3 * math.sin(tetaEarth)), 0)
    glRotatef(rangleEarth, 0, 0, 1)
    glutSolidSphere(0.5, 20, 20)

    # Ayın oluşturulması ve hem kendi hem de dünya etrafında dönmesi
    glColor(0.738, 0.738, 0.738)  # Ay için gri rengi
    glTranslatef((1 * math.cos(tetaMoon)), (1 * math.sin(tetaMoon)), 0)
    glRotatef(rangleMoon, 0, 0, 1)
    glutSolidSphere(0.2, 25, 25)
    glutSwapBuffers()
    glPopMatrix()

    # Açı değerlerinin arttırılması

    rangleSun += 0.01
    rangleEarth += 0.00001
    rangleMoon += 0.00002
    tetaEarth += 0.00040
    tetaMoon += 0.00080

    # Kendi kişisel laptobumu garantiye göndermeden önce test ettiğim değerler yoruma alınmayan değerler.
    # Aynı değerlerl ile düşük bir işlemciye sahip bilgisayarda test ettiğimde çok yavaş kaldı
    # Aşağıdaki değerler düşük bir işlemcideki normal dönme hızlarını veriyor
    # rangleSun += 2
    # rangleEarth += 2.5
    # rangleMoon += 3.0
    # tetaEarth += 0.01
    # tetaMoon += 0.007


def keyPressed(*args):
    # ESC tuşuna basınca programın sonlanması
    if args[0] == b"\x1b":
        sys.exit()
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Uzay Similasyonu")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutKeyboardFunc(keyPressed)

    InitGL()
    glutMainLoop()


main()