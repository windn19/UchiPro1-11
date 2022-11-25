import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class MainWindow(QWidget):
    """Класс окна"""
    def __init__(self):
        """Инициализация элементов"""
        # задание основных параметров окна
        super().__init__()
        self.move(700, 300)
        self.resize(300, 200)
        self.setWindowTitle("Кликер")

        # создание элементов
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # выравнивание надписи по горизонтали и вертикали

        # создание рамки и добавление в нее элементов
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)

        # добавление рамки в основное окно
        self.setLayout(vbox)

    def mousePressEvent(self, event):
        """Реакция на нажатие кнопки мыши"""
        self.label.setText(f'{event.x()}, {event.y()}')  # вывод в надписи координат окна

    def keyPressEvent(self, event):
        """Реакция на нажатие кнопки клавиатуры"""
        self.label.setText(event.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание приложения
    window = MainWindow()  # создание объекта класса нашего окна
    window.show()  # вывод на экран
    app.exec()
