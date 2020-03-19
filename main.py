from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
import sys
from PIL.ImageQt import ImageQt
from PIL import Image, ImageDraw
from design import Ui_Form as Design
from PyQt5 import QtGui
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore




class Widget(QWidget, Design):
    def __init__(self, im):
        super().__init__()
        self.setupUi(self)

        self.label.setPixmap(QPixmap.fromImage(ImageQt(im)))

width = int(input())
k = float(input())
n = int(input())
a = (0, 0)
b = (width, 0)
c = (width, width)
d = (0, width)
image = Image.new("RGBA", (width, width), (255, 255, 255, 255))
draw = ImageDraw.Draw(image)
draw.line((a, b), fill="red", width=5)
draw.line((b, c), fill="red", width=5)
draw.line((c, d), fill="red", width=5)
draw.line((d, a), fill="red", width=5)
for i in range(n - 1):
    o = (k * a[0], k * a[1])
    o1 = ((1 - k) * b[0], (1 - k) * b[1])
    z = (o[0] + o1[0], o[1] + o1[1])
    a = (round((k * a[0], k * a[1])[0] + ((1 - k) * b[0], (1 - k) * b[1])[0]), round((k * a[0], k * a[1])[1] + ((1 - k) * b[0], (1 - k) * b[1])[1]))
    b = (round((k * b[0], k * b[1])[0] + ((1 - k) * c[0], (1 - k) * c[1])[0]), round((k * b[0], k * b[1])[1] + ((1 - k) * c[0], (1 - k) * c[1])[1]))
    c = (round((k * c[0], k * c[1])[0] + ((1 - k) * d[0], (1 - k) * d[1])[0]), round((k * c[0], k * c[1])[1] + ((1 - k) * d[0], (1 - k) * d[1])[1]))
    d = (round((k * d[0], k * d[1])[0] + ((1 - k) * a[0], (1 - k) * a[1])[0]), round((k * c[0], k * d[1])[1] + ((1 - k) * a[0], (1 - k) * a[1])[1]))
    draw.line((a, b), fill="red", width=1)
    draw.line((b, c), fill="red", width=1)
    draw.line((c, d), fill="red", width=1)
    draw.line((d, a), fill="red", width=1)
image.show()
app = QApplication(sys.argv)
ex = Widget(image)
ex.show()
sys.exit(app.exec_())