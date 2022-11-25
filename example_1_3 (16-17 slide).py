import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class MainWindow(QWidget):
    """Класс окна"""

    def __init__(self):
        """Инициализация элементов"""
        # задание основных параметров окна
        super().__init__()
        self.move(700, 300)
        self.resize(300, 200)
        self.setWindowTitle("Кликер")

        # Добавление кнопки и ее размеров
        button = QPushButton("Нажми меня!", self)
        button.setGeometry(100, 100, 100, 30)

        # соединение сигнала "нажатие на кнопку" со слотом self.button_was_clicked
        button.clicked.connect(self.button_was_clicked)

        # объявление переменной счетчика
        self.counter = 1

    def button_was_clicked(self):
        """Вывод значения счетчика и увеличение его значения"""
        print(self.counter)
        self.counter += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание приложения
    window = MainWindow()  # создание объекта класса нашего окна
    window.show()  # вывод на экран
    app.exec()
