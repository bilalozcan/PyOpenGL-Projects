'''
    Küp Çizimi için yardımcı Kaynaklar:
                https://www3.ntu.edu.sg/home/ehchua/programming/opengl/CG_Examples.html
    Çaydanlık Tut-Döndür-Bırak için yardımcı Kaynaklar:
                http://www.lighthouse3d.com/tutorials/glut-tutorial/mouse-putting-it-all-together/
                https://programmersought.com/article/8224783407/
                https://en.wikibooks.org/wiki/OpenGL_Programming/Glescraft_4
    KÜPÜN 3D OLDUĞU ANLAŞILSIN DİYE X VE Y EKSENLERİ ETRAFINDA KENDİLİĞİNDEN DÖNMEKTEDİR
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

# Küp için gerekli değişkenler
Cube_angle = 0  # Küpün dönmesi gereken açı
Cube_scale = 1  # Küpün Yakınlaştırma Değeri
Cube_X = 0  # Küpün X Pozisyonu
Cube_Y = 0  # Küpün Y Pozisyonu

# Çaydanlık için gerekli değişkenler
Mouse_Left_Down = False  # Fare Sol Buton Tıklanma Durumu True/False
mouse_X = 0  # Mouse'un X Pozisyonu
mouse_Y = 0  # Mouse'un Y Pozisyonu
Camera_angle_X = 0  # Camera Açısının X eksenindeki açısı
Camera_angle_Y = 0  # Camera Açısının Y eksenindeki açısı


# Küpün düzgün gözükebilmesi için perspektif eklenmiştir
def InitGL():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


# 3D Küp Çizimi
def Cube():
    # Üst Yüzey - Brink Pembe
    glBegin(GL_QUADS)
    glColor3f(0.98, 0.37, 0.49)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    # Alt Yüzey - Limon Sarısı
    glColor3f(1.0, 0.94, 0.44)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Ön Yüzey - Koyu Kahverengi
    glColor3f(0.19, 0.0784, 0.0784)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Arka Yüzey - Mavi
    glColor3f(0.01, 0.62, 0.50)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    # Sol Yüzey - Turuncu
    glColor3f(1.0, .5, 0.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    # Sağ Yüzey - Beyaz
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()


def DrawGLScene():
    global Cube_angle, Cube_X, Cube_Y, Cube_scale
    global Camera_angle_X, Camera_angle_Y
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glViewport(0, 0, 400, 400)

    glPushMatrix()
    glTranslatef(Cube_X, Cube_Y, -5.6) # Küp X ve Y ekseninde hareket etme
    glRotatef(Cube_angle, 0.20, 0.57, 0) # Küp X ve Y ekseni etrafında dönme
    glScale(Cube_scale, Cube_scale, Cube_scale) # Küp Ölçekleme
    Cube() # Küp Ekrana Çizimi
    glPopMatrix()

    glViewport(400, 0, 400, 400)

    glPushMatrix()
    glColor3f(0, 0, 1)
    glTranslatef(0, 0, -3.5) # Çaydanlığın z ekseninde biraz geriye taşıma
    glRotatef(Camera_angle_X, 1, 0, 0) # Fare hareketine göre Çaydanlık X Ekseninde Döndürme
    glRotatef(Camera_angle_Y, 0, 1, 0) # Fare hareketine göre Çaydanlık Y Ekseninde Döndürme
    glutWireTeapot(1)
    glPopMatrix()

    Cube_angle += 0.05 # Küpün eksenler etrafında dönmesi için açı değerinin arttırılması

    glutSwapBuffers()


def keyPressed(*args):
    global Cube_X, Cube_Y

    if args[0] == b"\x1b":  # ESC tuşuna basınca programın sonlanması
        sys.exit()
    if args[0] == b"a" or args[0] == b"A":  # a-A tuşuna basınca küpün sola hareket etmesi
        Cube_X -= 0.1
    if args[0] == b"d" or args[0] == b"D":  # d-D tuşuna basınca küpün sağa hareket etmesi
        Cube_X += 0.1
    if args[0] == b"w" or args[0] == b"W":  # w-W tuşuna basınca küpün yukarı hareket etmesi
        Cube_Y += 0.1
    if args[0] == b"s" or args[0] == b"S":  # s-S tuşuna basınca küpün aşağı hareket etmesi
        Cube_Y -= 0.1
    glutPostRedisplay()


def MouseWheel(*args):
    global Cube_scale

    if args[1] == -1:  # Fare tekerleği aşağı çevrilince küpün küçülmesi
        Cube_scale -= 0.05
    elif args[1] == 1:  # Fare tekerleği yukarı çevrilince küpün büyümesi
        Cube_scale += 0.05
    else:
        pass
    glutPostRedisplay()


# Mouse tıklanma işlevlerini kontrol eder
# Mouse sol buton tıklandığında mouse'nin o anki pozisyonlarını saklar.
# Mouse sol butonun basılı olup olmama durumunu da saklar
def Mouse(mouse_button, mouse_state, x, y):
    global Mouse_Left_Down, mouse_X, mouse_Y
    mouse_X = x
    mouse_Y = y

    if mouse_button == GLUT_LEFT_BUTTON:
        if mouse_state == GLUT_DOWN:
            Mouse_Left_Down = True
            print("Fare Sol Tuş Tıklandı")
        if mouse_state == GLUT_UP:
            Mouse_Left_Down = False
            print("Fare Sol Tuş Bırakıldı")
    glutPostRedisplay()


# Farenin sol tuşu basılı tutulduğu sürece farenin basıldığı pozisyondan yeni pozisyona göre
# ve her değişim için X ve Y ekseni için dönme açı değerleri belirler.
# Fare sol tuşu bırakıldığında işlem sona erer
def Motion(x, y):
    global Camera_angle_X, Camera_angle_Y, mouse_X, mouse_Y
    Camera_angle_X = 0
    Camera_angle_Y = 0

    if Mouse_Left_Down:
        Camera_angle_Y += (x - mouse_X)
        Camera_angle_X += (y - mouse_Y)
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(800, 400)
    glutInitWindowPosition(400, 400)
    glutCreateWindow(b"Homework 6")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutKeyboardFunc(keyPressed)
    glutMouseWheelFunc(MouseWheel)
    glutMouseFunc(Mouse)
    glutMotionFunc(Motion)
    InitGL()
    glutMainLoop()


main()
