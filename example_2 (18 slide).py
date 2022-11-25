import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit


class MainWindow(QWidget):
    """Класс окна"""
    def __init__(self):
        """Инициализация элементов"""
        # задание основных параметров окна
        super().__init__()
        self.move(700, 300)
        self.resize(250, 150)
        self.setWindowTitle("Ввод текста")

        # создание элементов
        label = QLabel()
        line_edit = QLineEdit()
        # создание рамки выравнивания и добавление в нее элементов
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(line_edit)
        # добавление рамки в окно
        self.setLayout(vbox)

        # соединение сигнала "Изменение текста со слотом label.setText
        line_edit.textChanged.connect(label.setText)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание приложения
    window = MainWindow()  # создание объекта класса нашего окна
    window.show()  # вывод на экран
    app.exec()
