'''
    Yukarı ve Aşağı ok tuşları ile
    Sağ ViewPort'daki robotun kollarının
    hareket ettirilmesi
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

angle_omuz_dirsek = 0  # Omuz noktasından dönme açısı
angle_dirsek_el = 0  # Dirsek noktasından dönme açısı


def InitGL():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-11.0, 11.0, -11.0, 11.0)
    glMatrixMode(GL_MODELVIEW)


# Sol Üst Noktayı, çerçeve kalınlığını ve çerçevenin en-boy değerlerini alıp çizdiren fonksiyon(İçi Boş Dörtgen Çizdirir)
def DrawFrame(x, y, en, boy, width):
    glColor3f(0.439, 0.679, 0.278)
    glLineWidth(width)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)
    glVertex2f(x + boy, y)
    glVertex2f(x + boy, y - en)
    glVertex2f(x, y - en)
    glEnd()


# Bir insan modeli çizen fonksiyon, omuz noktasından ve dirsek noktasından dönmesi için parametre olarak açı değerleri alır
# Kafa, Boyun, Gövde Normal Sabit çizim; Omuz-Dirsek Uzvu, Dirsek Noktası ve Dirsek-El Uzvu beraber hareket eden bir yapı
# Aynı zamanda Dirsek-El Uzvu da kendi içinde ayrı hareket eden bir yapıdır.
# Omuz noktasından döndürünce bütün kol döner, dirsek noktasından döndürünce sadece Dirsek-El Uzvu  hareket eder
def DrawModelParam(angle_dirsek_el, angle_omuz_dirsek):
    glColor3f(0.356, 0.607, 0.835)

    glBegin(GL_QUADS)  # Kafa Çizimi
    glVertex2f(-2, 4)
    glVertex2f(2, 4)
    glVertex2f(2, 1)
    glVertex2f(-2, 1)
    glEnd()

    glBegin(GL_QUADS)  # Boyun Çizimi
    glVertex2f(-0.5, 1)
    glVertex2f(0.5, 1)
    glVertex2f(0.5, -0.5)
    glVertex2f(-0.5, -0.5)
    glEnd()

    glBegin(GL_QUADS)  # Gövde Çizimi
    glVertex2f(-1.5, -0.5)
    glVertex2f(1.5, -0.5)
    glVertex2f(1.5, -5)
    glVertex2f(-1.5, -5)
    glEnd()

    glPushMatrix()  # --------- Sol Kol Çizim Başlangıç ----------------------
    glTranslatef(-1.3, -0.85, 0)  # Dönme noktasının Omuz noktasına ötelenmesi
    glRotatef(angle_omuz_dirsek, 0, 0, 1)  # z ekseni etrafında verilen açıda dönmesi (Omuz noktasında)

    glBegin(GL_QUADS)  # Sol Omuz-Dirsek Uzvunun Çizimi
    glVertex2f(-2.5, 0.35)
    glVertex2f(0, 0.35)
    glVertex2f(0, -0.35)
    glVertex2f(-2.5, -0.35)
    glEnd()

    glTranslatef(-2.3, 0, 0)
    glutSolidSphere(0.45, 50, 50)  # Sol Dirsek Noktası için Daire Çizimi

    glPushMatrix()  # -- Sol Dirsek-El Çizim Başlangıç ------

    glTranslatef(0, 0, 0)  # Dönme noktasının dirsek noktasına ötelenmesi
    glRotatef(-angle_dirsek_el, 0, 0, 1)  # z ekseni etrafında verilen açıda dönmesi (Dirsek noktasında)

    glBegin(GL_QUADS)  # Sol Dirsek-El Uzvunun Çizimi
    glVertex2f(-2.5, 0.35)
    glVertex2f(0, 0.35)
    glVertex2f(0, -0.35)
    glVertex2f(-2.5, -0.35)
    glEnd()
    glPopMatrix()  # -- Sol Dirsek-El Çizim Bitiş ------------

    glPopMatrix()  # --------- Sol Kol Çizim Bitiş --------------------------

    glPushMatrix()  # -------- Sağ Kol Çizim Başlangıç ----------------------
    glTranslatef(1.3, -0.85, 0)  # Dönme noktasının Omuz noktasına ötelenmesi
    glRotatef(-angle_omuz_dirsek, 0, 0, 1)  # z ekseni etrafında verilen açıda dönmesi (Omuz noktasında)

    glBegin(GL_QUADS)  # Sağ Omuz-Dirsek Uzvunun Çizimi
    glVertex2f(0, 0.35)
    glVertex2f(2.5, 0.35)
    glVertex2f(2.5, -0.35)
    glVertex2f(0, -0.35)
    glEnd()

    glTranslatef(2.3, 0, 0)
    glutSolidSphere(0.45, 50, 50)  # Sağ Dirsek Noktası için Daire Çizimi

    glPushMatrix()  # -- Sağ Dirsek-El Çizim Başlangıç ------
    glTranslatef(0, 0, 0)  # Dönme noktasının dirsek noktasına ötelenmesi
    glRotatef(angle_dirsek_el, 0, 0, 1)  # z ekseni etrafında verilen açıda dönmesi (Dirsek noktasında)
    glBegin(GL_QUADS)
    glVertex2f(0, 0.35)
    glVertex2f(2.5, 0.35)
    glVertex2f(2.5, -0.35)
    glVertex2f(0, -0.35)
    glEnd()
    glPopMatrix()  # -- Sağ Dirsek-El Çizim Başlangıç --------

    glPopMatrix()  # --------- Sağ Kol Çizim Bitiş -------------------------


def DrawGLScene():
    global angle_dirsek_el, angle_omuz_dirsek
    glClear(GL_COLOR_BUFFER_BIT)

    glViewport(0, 0, 400, 400)  # Soldaki Ekran
    DrawFrame(-11, 11, 22, 22, 8)  # Sol ViewPort İçin Kare Çerçeve
    DrawModelParam(0, 0)  # Dönmeyen kol çizimi için 0,0 parametreleri ile model çizimi

    glViewport(400, 0, 400, 400)  # Sağdaki Ekran
    DrawFrame(-11, 11, 22, 22, 8)  # Sağ ViewPort İçin Kare Çerçeve
    DrawModelParam(angle_dirsek_el, angle_omuz_dirsek)  # Dönen kol için global değişkenler ile kol çizimi

    glutSwapBuffers()


def specialFunc(key, x, y):
    global angle_dirsek_el, angle_omuz_dirsek
    if key == GLUT_KEY_UP:  # Yukarı Ok Tuşuna Basılırsa Kol ve Omzun yukarı hareket etmesi
        angle_dirsek_el += 10
        angle_omuz_dirsek -= 3
    if key == GLUT_KEY_DOWN:  # Aşağı Ok Tuşuna Basılırsa Kol ve Omzun aşağı hareket etmesi
        angle_dirsek_el -= 10
        angle_omuz_dirsek += 3
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(800, 400)
    glutInitWindowPosition(400, 400)
    glutCreateWindow(b"Vize Bilal Ozcan")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutSpecialFunc(specialFunc)
    InitGL()
    glutMainLoop()


main()
