import sys

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QLCDNumber


class MiniCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.number_1 = QLineEdit(self)
        self.number_2 = QLineEdit(self)

        self.calculate_button = QPushButton('->', self)
        self.calculate_button.clicked.connect(self.eval)

        self.result_sum = QLCDNumber()
        self.result_sub = QLCDNumber()
        self.result_mul = QLCDNumber()
        self.result_div = QLCDNumber()

        h_layout = QHBoxLayout()

        v_layout1 = QVBoxLayout()
        v_layout2 = QVBoxLayout()
        v_layout3 = QVBoxLayout()
        v_layout4 = QVBoxLayout()

        self.label1 = QLabel('Первое число(целое):')
        v_layout1.addWidget(self.label1)
        v_layout1.addWidget(self.number_1)
        self.label2 = QLabel('Второе число(целое):')
        v_layout1.addWidget(self.label2)
        v_layout1.addWidget(self.number_2)

        v_layout2.addWidget(self.calculate_button)

        self.sum = QLabel('Сумма:')
        v_layout3.addWidget(self.sum)
        self.sub = QLabel('Разность:')
        v_layout3.addWidget(self.sub)
        self.mul = QLabel('Произведение:')
        v_layout3.addWidget(self.mul)
        self.div = QLabel('Частность:')
        v_layout3.addWidget(self.div)

        v_layout4.addWidget(self.result_sum)
        v_layout4.addWidget(self.result_sub)
        v_layout4.addWidget(self.result_mul)
        v_layout4.addWidget(self.result_div)

        h_layout.addLayout(v_layout1)
        h_layout.addLayout(v_layout2)
        h_layout.addLayout(v_layout3)
        h_layout.addLayout(v_layout4)

        self.setLayout(h_layout)

        self.setWindowTitle('Миникалькулятор')
        self.setGeometry(100, 100, 400, 100)

    def eval(self):
        try:
            num1 = int(self.number_1.text())
            num2 = int(self.number_2.text())
            sender = self.sender()
            if sender.text() == '->':
                summ = num1 + num2
                self.result_sum.display(summ)
                subb = num1 - num2
                self.result_sub.display(subb)
                mull = num1 * num2
                self.result_mul.display(mull)
                divv = num1 / num2
                self.result_div.display(float(divv))
        except ZeroDivisionError:
            self.result_div.display('Error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MiniCalculator()
    ex.show()
    sys.exit(app.exec())