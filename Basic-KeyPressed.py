'''
    R-G-B tuşlarına basıldığında ilgili arabanın ilgili renge boyanması
    R:Kırmızı
    G:Yeşil
    B:Mavi
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import random as rn

DEG2RAD = 3.14159 / 180  # Dereceden radyana çevirim

# Araba başlangıç rengi için rastgele R, G, B değerlerinin belirlenmesi
R = rn.random()
G = rn.random()
B = rn.random()


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-6.0, 6.0, -6.0, 6.0)


# Sol Üst Noktayı ve dörtgenin en-boy değerlerini alıp çizdiren fonksiyon
def rectangleDraw(x, y, en, boy):
    glColor3f(R, G, B)
    glPointSize(2.0)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + boy, y)
    glVertex2f(x + boy, y - en)
    glVertex2f(x, y - en)

    glEnd()


# Orijinden  x ve  y uzaklıkta verilen yarıçapda daire çizdiren fonksiyon
def drawCircle(x, y, radius):
    glColor3f(0, 0, 0)
    glBegin(GL_POLYGON)
    for i in range(360):
        degInRad = i * DEG2RAD
        glVertex2f((cos(degInRad) * radius) - x, (sin(degInRad) * radius) - y)
    glEnd()


# Sol Üst Noktayı çerçeve kalınlığını ve çerçevenin en-boy değerlerini alıp çizdiren fonksiyon(İçi Boş Dörtgen Çizdirir)
def drawFrame(x, y, en, boy, width):
    glColor3f(0, 0, 0)
    glLineWidth(width)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)
    glVertex2f(x + boy, y)
    glVertex2f(x + boy, y - en)
    glVertex2f(x, y - en)
    glEnd()


# Araba için gerekli parça çizimlerini yapan fonksiyon
def draw():
    print("Draw Func:")
    glClear(GL_COLOR_BUFFER_BIT)
    drawFrame(-3, 3, 3, 6, 6)
    rectangleDraw(-3, 3, 3, 6)
    drawCircle(3.8, 3.5, 0.7)
    drawCircle(-3.8, 3.5, 0.7)
    drawFrame(-5, 0, 3, 5, 6)
    rectangleDraw(-5, 0, 3, 5)
    drawFrame(0, 0, 3, 5, 6)
    rectangleDraw(0, 0, 3, 5)
    drawFrame(-6, 6, 12, 12, 25)
    drawFrame(-5.6, 5.6, 11.2, 11.2, 4)

    glFlush()


def keyPressed(*args):
    global R, G, B
    print(args[0])
    if args[0] == b"\x1b":
        sys.exit()
    elif args[0] == b"r":
        print("RED")
        R = 1
        G = 0
        B = 0
    elif args[0] == b"g":
        print("GREEN")
        R = 0
        G = 1
        B = 0
    elif args[0] == b"b":
        print("BLUE")
        R = 0
        G = 0
        B = 1

    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 500)
    glutInitWindowPosition(70, 50)
    glutCreateWindow("Homework")
    glutDisplayFunc(draw)
    glutKeyboardFunc(keyPressed)
    init()
    glutMainLoop()


main()
