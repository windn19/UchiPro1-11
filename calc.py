from operator import sub, mul, truediv, add
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QLabel, QPushButton, QGridLayout, QVBoxLayout


class Calcul(QWidget):
    def __init__(self):
        super().__init__()
        self.move(700, 200)
        self.resize(300, 300)
        self.setWindowTitle("Калькулятор")

        vbox = QVBoxLayout()
        self.lcd = QLCDNumber(self)
        self.label = QLabel(self)
        self.lcd.setMaximumHeight(200)
        self.label.setMaximumHeight(30)

        vbox.addWidget(self.label)
        vbox.addWidget(self.lcd)

        grid = QGridLayout()
        self.op = ['+', '-', '*', '/', '=']
        btn = QPushButton('C', self)
        grid.addWidget(btn, 0, 0, 1, 3)
        btn.clicked.connect(self.click_c)

        btn = QPushButton('/', self)
        grid.addWidget(btn, 0, 3)
        btn.clicked.connect(self.click_btn)
        nums = ['7', '8', '9', '*', '4', '5', '6', '-', '1', '2', '3', '+']
        for num, ch in enumerate(nums):
            btn = QPushButton(self)
            btn.setText(ch)
            grid.addWidget(btn, (num // 4) + 1, num % 4)
            btn.clicked.connect(self.click_btn)

        btn = QPushButton('0', self)
        grid.addWidget(btn, 4, 0, 1, 3)
        btn.clicked.connect(self.click_btn)

        btn = QPushButton('=', self)
        grid.addWidget(btn, 4, 3)
        btn.clicked.connect(self.click_btn)

        vbox.addLayout(grid)
        self.setLayout(vbox)
        self.shutdown()
        self.numer = ''
        self.expression = ''

    def click_btn(self):
        obj = self.sender()
        t = obj.text()
        if t not in self.op:
            if not self.expression:
                self.numer = t
                self.shutdown()
            else:
                self.numer += t
            self.expression += t
            self.lcd.display(self.numer)
            self.label.setText(self.expression)
        else:
            self.click_oper(obj, t)

    def click_oper(self, op, t):
        alias = {'+': add,
                 '-': sub,
                 '/': truediv,
                 '*': mul}
        self.expression += t
        if not self.num1:
            if t == '=':
                self.expression = ''
                return
            self.num1 = int(self.numer)
            self.oper = alias[t]
            self.numer = ''
        else:
            self.num2 = int(self.numer)
            try:
                self.numer = str(self.oper(self.num1, self.num2))
                self.shutdown()
            except:
                self.numer = 'Error'
            self.expression = ''
        self.lcd.display(self.numer)
        self.label.setText(self.expression)

    def click_c(self):
        self.shutdown()
        self.numer = ''
        self.expression = ''
        self.lcd.display(self.numer)
        self.label.setText(self.expression)

    def shutdown(self):
        self.num1 = None
        self.num2 = None
        self.oper = None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calcul()
    window.show()
    app.exec()
