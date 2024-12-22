import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
import random
from UI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw_circles)
        self.circles = []

    def draw_circles(self):
        diameter = random.randint(10, 250)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.circles.append((x, y, diameter, r, g, b))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            x, y, diameter, r, g, b = circle
            painter.setBrush(QColor(r, g, b))
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
