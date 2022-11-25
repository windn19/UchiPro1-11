import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLCDNumber, QHBoxLayout, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.lcd = QLCDNumber(self)
        self.button_0 = QPushButton("0", self)
        self.button_1 = QPushButton("1", self)
        self.button_2 = QPushButton("2", self)
        self.button_3 = QPushButton("3", self)
        self.button_4 = QPushButton("4", self)
        self.button_5 = QPushButton("5", self)
        self.button_6 = QPushButton("6", self)
        self.button_7 = QPushButton("7", self)
        self.button_8 = QPushButton("8", self)
        self.button_9 = QPushButton("9", self)
        self.button_plus = QPushButton("+", self)
        self.button_minus = QPushButton("-", self)
        self.button_mul = QPushButton("*", self)
        self.button_div = QPushButton("/", self)
        self.button_equal = QPushButton("=", self)
        # свяжите сигналы виджетов с нужными функциями
        # например self.button_0.clicked.connect(self.number_click)
        # ...
        self.expression = ''  # строка с арифметическим выражением
        self.number = ''  # строка с числом для вывода в QLCDNumber
        self.init_ui()

    def init_ui(self):
        self.resize(250, 500)
        self.setWindowTitle("Калькулятор")
        self.lcd.setMaximumHeight(200)
        self.label.setMaximumHeight(30)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.lcd, 5)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_0)
        hbox.addWidget(self.button_1)
        hbox.addWidget(self.button_2)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_3)
        hbox.addWidget(self.button_4)
        hbox.addWidget(self.button_5)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_6)
        hbox.addWidget(self.button_7)
        hbox.addWidget(self.button_8)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_plus)
        hbox.addWidget(self.button_9)
        hbox.addWidget(self.button_minus)
        vbox.addLayout(hbox)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button_mul)
        hbox.addWidget(self.button_div)
        hbox.addWidget(self.button_equal)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def number_click(self):
        """
        Функция для обработки сигналов нажатия на кнопки с цифрами.
        """
        # допишите код функции
        # ...

    def operation_click(self):
        """
        Функция для обработки сигналов нажатия на кнопки с действиями.
        """
        # допишите код функции
        # ...

    def keyPressEvent(self, event):
        """
        Функция обработчик нажатия клавиши.
        """
        # допишите код функции
        # ...


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание приложения
    window = MainWindow()  # создание объекта класса нашего окна
    window.show()  # вывод на экран
    app.exec()