from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from random import randint

def getNumber():
    rand_number = randint(0, 99)
    number.setText(str(rand_number))
    winner.setText('Победитель:')

def surprize():
    label.show()


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определи победителя')
main_win.resize(500, 300)

button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')
button6 = QPushButton('6')

button4.clicked.connect(surprize)

v_layout = QVBoxLayout()

h1_layout = QHBoxLayout()
h2_layout = QHBoxLayout()
h3_layout = QHBoxLayout()

h1_layout.addWidget(button1, alignment=Qt.AlignLeft)
h1_layout.addWidget(button2, alignment=Qt.AlignRight)

h2_layout.addWidget(button3, alignment=Qt.AlignLeft)
h2_layout.addWidget(button4, alignment=Qt.AlignRight)

h3_layout.addWidget(button5, alignment=Qt.AlignLeft)
h3_layout.addWidget(button6, alignment=Qt.AlignRight)

label = QLabel('Сюрприз')
# label.hide()
# v_layout.addWidget(label, alignment=Qt.AlignCenter)


v_layout.addLayout(h1_layout)
v_layout.addLayout(h2_layout)
v_layout.addLayout(h3_layout)

main_win.setLayout(v_layout)

main_win.show()
app.exec_()
