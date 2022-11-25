import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


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
        button_1 = QPushButton("Нажми меня 1", self)
        button_2 = QPushButton("Нажми меня 2", self)

        # создание рамки и добавление в нее элементов
        vbox = QVBoxLayout()
        vbox.addWidget(button_1)
        vbox.addWidget(button_2)

        # добавление рамки в основное окно
        self.setLayout(vbox)

        # соединение сигнала "нажатие на кнопку" со слотом self.button_was_clicked у первой и второй кнопки
        button_1.clicked.connect(self.button_was_clicked)
        button_2.clicked.connect(self.button_was_clicked)

    def button_was_clicked(self):
        """Обработка нажатия на кнопку"""
        sender = self.sender()  # определение объекта, который вызвал сигнал
        print(sender.text())  # вывода его текста в терминале


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание приложения
    window = MainWindow()  # создание объекта класса нашего окна
    window.show()  # вывод на экран
    app.exec()
