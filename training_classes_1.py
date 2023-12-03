from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([]) #сторюємо віконний додаток
win = QWidget() # створємо вікно
win.resize(400, 200)
win.setWindowTitle("Генератор переможця")

winner = QLabel("Номер переможця:")
result = QLabel("?")

gen_btn = QPushButton("Згенерувати")

line = QVBoxLayout()
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(result, alignment=Qt.AlignCenter)
line.addWidget(gen_btn, alignment=Qt.AlignCenter)

win.setLayout(line)

# вкінці
win.show() #показує вікно
app.exec_() # запускаємо додаток


